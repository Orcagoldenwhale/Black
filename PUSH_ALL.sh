#!/bin/bash

echo "🚀 Выгрузка всего кода в репозиторий black..."
echo ""

cd "/Users/simonshmelev/Desktop/мой проект"

# Настраиваем remote
git remote set-url origin https://github.com/Orcagoldenwhale/black.git

echo "📤 Отправка кода..."
echo ""
echo "⚠️  Если запросит авторизацию:"
echo "   Username: Orcagoldenwhale"
echo "   Password: ваш токен (github_pat_...)"
echo ""

git push -u origin main --force

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ УСПЕШНО! Код выгружен!"
    echo ""
    echo "🔗 Теперь настройте GitHub Pages:"
    echo "   https://github.com/Orcagoldenwhale/black/settings/pages"
    echo ""
    echo "   Branch: main"
    echo "   Folder: / (root)"
    echo "   Нажмите Save"
    echo ""
    echo "📱 Ваша ссылка (через 1-2 минуты):"
    echo "   https://orcagoldenwhale.github.io/black/blackjack.html?style=casino"
else
    echo ""
    echo "❌ Ошибка авторизации."
    echo ""
    echo "💡 Возможные причины:"
    echo "   1. Токен не имеет прав на запись"
    echo "   2. Токен истек"
    echo "   3. Нужно создать новый токен с правами 'repo'"
    echo ""
    echo "📋 Создайте новый токен:"
    echo "   https://github.com/settings/tokens"
    echo "   Выберите 'repo' (Full control)"
fi

