#!/bin/bash

echo "🚀 Выгрузка кода в репозиторий black..."

cd "/Users/simonshmelev/Desktop/мой проект"

# Настраиваем remote
git remote set-url origin https://github.com/Orcagoldenwhale/black.git

echo ""
echo "📤 Отправка кода..."
echo "При запросе авторизации используйте:"
echo "  Username: Orcagoldenwhale"
echo "  Password: ваш токен (github_pat_...)"
echo ""

git push -u origin main --force

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ УСПЕШНО! Код выгружен!"
    echo ""
    echo "🔗 Теперь настройте GitHub Pages:"
    echo "   https://github.com/Orcagoldenwhale/black/settings/pages"
    echo ""
    echo "   Branch: main, Folder: / (root)"
    echo "   Нажмите Save"
    echo ""
    echo "📱 Ваша ссылка будет:"
    echo "   https://orcagoldenwhale.github.io/black/blackjack.html?style=casino"
else
    echo ""
    echo "❌ Ошибка. Попробуйте выполнить команду вручную:"
    echo "   git push -u origin main --force"
fi

