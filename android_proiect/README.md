# Proiect Android separat de "interfete"

Acest folder conține un proiect Android minimal, separat de aplicația existentă din repository.

## Cum folosești un environment separat

1. Păstrează acest proiect în folderul `android_proiect/`.
2. Deschide folderul direct în Android Studio (`File > Open`).
3. Nu amesteca fișierele cu aplicația Python din `aplicatie/` — fiecare proiect are propriile fișiere.

## Structura aplicației

Aplicația include 6 ecrane (activități) cu navigare prin butoane:
- Autentificare
- Meniu principal
- Gestionare date
- Test grilă
- Informații
- Ajutor

Fiecare ecran afișează numele studentului și grupa în bara de titlu (Toolbar), conform cerințelor din `INSTRUCTIUNI.MD`.

> Actualizează string-ul `student_title` din `app/src/main/res/values/strings.xml` cu numele și grupa ta.
