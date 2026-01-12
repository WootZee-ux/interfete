"""Utilitare pentru autentificare si gestionarea parolelor."""
from __future__ import annotations

import hashlib
import secrets
from pathlib import Path

USERS_FILE = Path(__file__).resolve().parent / "storage" / "users.htpasswd"


def _hash_password(password: str, salt: str | None = None) -> str:
    if salt is None:
        salt = secrets.token_hex(8)
    digest = hashlib.sha256(f"{salt}{password}".encode("utf-8")).hexdigest()
    return f"sha256${salt}${digest}"


def _verify_password(password: str, stored_hash: str) -> bool:
    parts = stored_hash.split("$")
    if len(parts) != 3 or parts[0] != "sha256":
        return False
    _, salt, digest = parts
    return hashlib.sha256(f"{salt}{password}".encode("utf-8")).hexdigest() == digest


def verify_credentials(username: str, password: str) -> bool:
    if not USERS_FILE.exists():
        return False
    user_map = _load_users()
    stored_hash = user_map.get(username)
    if not stored_hash:
        return False
    return _verify_password(password, stored_hash)


def update_password(username: str, new_password: str) -> bool:
    if not USERS_FILE.exists():
        return False
    lines = USERS_FILE.read_text(encoding="utf-8").splitlines()
    updated = False
    hashed_password = _hash_password(new_password)
    updated_lines: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in line:
            updated_lines.append(line)
            continue
        current_user, _ = line.split(":", 1)
        if current_user == username:
            updated_lines.append(f"{username}:{hashed_password}")
            updated = True
        else:
            updated_lines.append(line)
    if not updated:
        return False
    USERS_FILE.write_text("\n".join(updated_lines) + "\n", encoding="utf-8")
    return True


def _load_users() -> dict[str, str]:
    users: dict[str, str] = {}
    for line in USERS_FILE.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in line:
            continue
        username, stored_hash = line.split(":", 1)
        users[username] = stored_hash
    return users
