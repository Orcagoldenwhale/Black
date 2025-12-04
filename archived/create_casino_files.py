#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для создания упрощенных файлов только с режимом Casino
"""

import re

def create_blackjack_casino():
    """Создает blackjack-casino.html только с режимом Casino"""
    print("Создаю blackjack-casino.html...")
    
    with open('blackjack.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # TODO: Реализовать удаление ненужных частей
    # Пока просто сообщу, что нужно сделать
    
    print("Файл будет создан вручную...")
    return True

if __name__ == '__main__':
    create_blackjack_casino()
