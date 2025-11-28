# 🚀 Финальная выгрузка кода

## ⚠️ Проблема с токеном

Текущий токен (fine-grained) не имеет прав на запись в репозиторий.

## ✅ Решение: Выполните вручную в терминале

```bash
cd "/Users/simonshmelev/Desktop/мой проект"
git remote set-url origin https://github.com/Orcagoldenwhale/Black.git
git push -u origin main --force
```

**При запросе авторизации:**
- Username: `Orcagoldenwhale`
- Password: `[ваш токен]`

---

## 🔧 Если токен не работает:

Создайте **Classic Token** с правами `repo`:

1. https://github.com/settings/tokens
2. "Generate new token (classic)"
3. Отметьте **"repo"** (Full control)
4. Используйте новый токен

---

## ✅ После успешной выгрузки:

1. Настройте GitHub Pages:
   - https://github.com/Orcagoldenwhale/Black/settings/pages
   - Branch: `main`, Folder: `/ (root)`
   - Save

2. Ваша ссылка (через 1-2 минуты):
   - **https://orcagoldenwhale.github.io/Black/blackjack.html?style=casino**

