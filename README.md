# עוזרת הפרדס — שרת

## הוראות פריסה על Render

1. לך ל-render.com והירשם חינם
2. לחץ "New" → "Web Service"
3. חבר ל-GitHub repository שלך (העלה את הקבצים האלה)
4. בחר Python כ-Environment
5. הוסף Environment Variable:
   - Key: ANTHROPIC_API_KEY
   - Value: המפתח שלך מ-console.anthropic.com
6. לחץ Deploy

## קבצים
- app.py — השרת הראשי
- data_general.py — מאגר משרד החקלאות
- data_shoham.py — מאגר שוהם, אורי
- requirements.txt — תלויות
