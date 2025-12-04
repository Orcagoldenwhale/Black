#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для создания упрощенных файлов только с режимом Casino
Удаляет переключатели игр, переключатели стилей, старые стили и старую таблицу
"""

import re

def create_blackjack_casino():
    """Создает blackjack-casino.html только с режимом Casino"""
    print("Создаю blackjack-casino.html...")
    
    with open('blackjack.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Удаляем переключатель игр (HTML)
    content = re.sub(r'<!-- Переключатель игр -->.*?<!-- Переключатель стилей -->', '', content, flags=re.DOTALL)
    
    # Удаляем переключатель стилей (HTML)
    content = re.sub(r'<!-- Переключатель стилей -->.*?<div class="casino-table"', '  <div class="casino-table"', content, flags=re.DOTALL)
    
    # Удаляем CSS для переключателей игр
    content = re.sub(r'/\* Переключатель игр \*/.*?\.game-btn\.active \{.*?\n.*?\}', '', content, flags=re.DOTALL)
    
    # Удаляем CSS для переключателей стилей
    content = re.sub(r'/\* Переключатель стилей \*/.*?\.style-btn\.active \{.*?\n.*?\}', '', content, flags=re.DOTALL)
    
    # Удаляем все стили для Classic/Modern/Luxury
    content = re.sub(r'/\* СТИЛЬ: CLASSIC \*/.*?\.style-classic \.old-section-label \{.*?\n.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'/\* СТИЛЬ: MODERN \*/.*?\.style-modern \.old-section-label \{.*?\n.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'/\* СТИЛЬ: LUXURY \*/.*?\.style-luxury \.old-section-label \{.*?\n.*?\}', '', content, flags=re.DOTALL)
    
    # Удаляем старую таблицу (HTML)
    content = re.sub(r'<!-- Старый стиль стола.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    
    # Удаляем CSS для старой таблицы
    content = re.sub(r'/\* Старый стиль стола.*?\.old-deck-count \{.*?\n.*?\}', '', content, flags=re.DOTALL)
    
    # Удаляем JavaScript для старого стиля
    content = re.sub(r'// Инициализация старого стиля.*?oldUpdateButtons\(\);', '', content, flags=re.DOTALL)
    
    # Удаляем переключение стилей из JS
    content = re.sub(r'// Переключение стилей.*?window\.history\.replaceState.*?\}\);', '', content, flags=re.DOTALL)
    
    # Удаляем ссылки на oldHitBtn, oldStandBtn и т.д. из CSS
    content = re.sub(r'\.control-btn\[id="oldHitBtn"\].*?\n', '', content)
    content = re.sub(r'\.control-btn\[id="oldStandBtn"\].*?\n', '', content)
    content = re.sub(r'\.control-btn\[id="oldDealBtn"\].*?\n', '', content)
    content = re.sub(r'\.control-btn\[id="oldDoubleBtn"\].*?\n', '', content)
    
    # Обновляем body класс - убираем style-casino, просто body
    content = re.sub(r'<body class="style-casino">', '<body>', content)
    content = re.sub(r'body\.style-casino', 'body', content)
    
    # Убираем условное отображение casino-table
    content = re.sub(r'body\.style-casino \.casino-table \{.*?display: block;.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'body\.style-casino \.old-style-table \{.*?display: none;.*?\}', '', content, flags=re.DOTALL)
    
    # Убираем из медиа-запросов упоминания переключателей
    content = re.sub(r'\.game-switcher \{.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\.game-btn \{.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\.style-switcher \{.*?\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\.style-btn \{.*?\}', '', content, flags=re.DOTALL)
    
    # Изменяем background body на Casino
    content = re.sub(r'body \{.*?background: #0d1b1f;.*?\}', 
                     'body {\n      font-family: \'Montserrat\', sans-serif;\n      background: linear-gradient(135deg, #1a0000 0%, #330000 100%);\n      min-height: 100vh;\n      display: flex;\n      justify-content: center;\n      align-items: center;\n      padding: 20px;\n      overflow-x: hidden;\n      position: relative;\n    }', 
                     content, flags=re.DOTALL)
    
    with open('blackjack-casino.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ blackjack-casino.html создан!")

if __name__ == '__main__':
    create_blackjack_casino()

