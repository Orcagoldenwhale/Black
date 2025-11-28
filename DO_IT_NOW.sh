#!/bin/bash

echo "🚀 Выгрузка проекта на GitHub..."
echo ""

cd "/Users/simonshmelev/Desktop/мой проект"

echo "📤 Отправка кода на GitHub..."
git push -u origin main --force

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ УСПЕШНО! Код выгружен на GitHub!"
    echo ""
    echo "🔗 Ваша ссылка на Блэкджек - режим Casino:"
    echo "   https://orcagoldenwhale.github.io/video-timestamp-app/blackjack.html?style=casino"
    echo ""
    echo "📋 Теперь настройте GitHub Pages:"
    echo "   1. Откройте: https://github.com/Orcagoldenwhale/video-timestamp-app/settings/pages"
    echo "   2. Branch: main, Folder: / (root)"
    echo "   3. Нажмите Save"
    echo "   4. Подождите 1-2 минуты"
else
    echo ""
    echo "❌ Ошибка при отправке. Нужна авторизация."
    echo ""
    echo "💡 Создайте Personal Access Token:"
    echo "   https://github.com/settings/tokens"
    echo ""
    echo "   Затем запустите этот скрипт снова или выполните:"
    echo "   git push -u origin main --force"
fi

