#!/bin/bash

echo "🚀 Выгрузка проекта на GitHub..."
echo ""

# Проверяем, существует ли remote
if git remote get-url origin > /dev/null 2>&1; then
    echo "✅ Remote 'origin' уже настроен"
    git remote -v
else
    echo "❌ Remote не найден. Добавляем..."
    git remote add origin https://github.com/Orcagoldenwhale/video-timestamp-app.git
fi

echo ""
echo "📤 Отправка кода на GitHub..."
echo ""
echo "⚠️  Если потребуется авторизация:"
echo "   Username: ваш GitHub username"
echo "   Password: Personal Access Token (НЕ ваш пароль!)"
echo ""
echo "   Создайте токен здесь: https://github.com/settings/tokens"
echo "   Выберите: repo (полный доступ к репозиториям)"
echo ""

# Пытаемся сделать push
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Успешно! Код выгружен на GitHub"
    echo "🔗 Репозиторий: https://github.com/Orcagoldenwhale/video-timestamp-app"
else
    echo ""
    echo "❌ Ошибка при отправке. Возможные причины:"
    echo "   1. Репозиторий не существует на GitHub - создайте его на https://github.com/new"
    echo "   2. Нужна авторизация - используйте Personal Access Token"
    echo "   3. Нет прав доступа к репозиторию"
    echo ""
    echo "💡 Попробуйте выполнить команду вручную:"
    echo "   git push -u origin main"
fi

