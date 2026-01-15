"""Utilitare pentru autentificare si gestionarea parolelor."""
from __future__ import annotations

import hashlib
import secrets
from pathlib import Path

FISIER_UTILIZATORI = Path(__file__).resolve().parent / "stocare" / "utilizatori.htpasswd"


def _hash_parola(parola: str, salt: str | None = None) -> str:
    if salt is None:
        salt = secrets.token_hex(8)
    digest = hashlib.sha256(f"{salt}{parola}".encode("utf-8")).hexdigest()
    return f"sha256${salt}${digest}"


def _verifica_parola(parola: str, hash_salvat: str) -> bool:
    parti = hash_salvat.split("$")
    if len(parti) != 3 or parti[0] != "sha256":
        return False
    _, salt, digest = parti
    return hashlib.sha256(f"{salt}{parola}".encode("utf-8")).hexdigest() == digest


def verifica_credentiale(utilizator: str, parola: str) -> bool:
    if not FISIER_UTILIZATORI.exists():
        return False
    utilizatori = _incarca_utilizatori()
    hash_salvat = utilizatori.get(utilizator)
    if not hash_salvat:
        return False
    return _verifica_parola(parola, hash_salvat)


def actualizeaza_parola(utilizator: str, parola_noua: str) -> bool:
    if not FISIER_UTILIZATORI.exists():
        return False
    linii = FISIER_UTILIZATORI.read_text(encoding="utf-8").splitlines()
    actualizat = False
    parola_hash = _hash_parola(parola_noua)
    linii_actualizate: list[str] = []
    for linie in linii:
        linie_curata = linie.strip()
        if not linie_curata or linie_curata.startswith("#") or ":" not in linie:
            linii_actualizate.append(linie)
            continue
        utilizator_curent, _ = linie.split(":", 1)
        if utilizator_curent == utilizator:
            linii_actualizate.append(f"{utilizator}:{parola_hash}")
            actualizat = True
        else:
            linii_actualizate.append(linie)
    if not actualizat:
        return False
    FISIER_UTILIZATORI.write_text("\n".join(linii_actualizate) + "\n", encoding="utf-8")
    return True


def _incarca_utilizatori() -> dict[str, str]:
    utilizatori: dict[str, str] = {}
    for linie in FISIER_UTILIZATORI.read_text(encoding="utf-8").splitlines():
        linie_curata = linie.strip()
        if not linie_curata or linie_curata.startswith("#") or ":" not in linie:
            continue
        utilizator, hash_salvat = linie.split(":", 1)
        utilizatori[utilizator] = hash_salvat
    return utilizatori
