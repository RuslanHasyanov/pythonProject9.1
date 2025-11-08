import pytest
import re
from your_module import get_mask_card_number  # Замените your_module на имя вашего модуля


@pytest.mark.parametrize("invalid_input", [
    "",  # Пустая строка
    "   ",  # Только пробелы



    def test_empty_string(self):
        """Тестирование обработки пустой строки"""
        with pytest.raises(ValueError):
            get_mask_card_number("")

    def test_whitespace_string(self):
        """Тестирование обработки строки с пробелами"""
        with pytest.raises(ValueError):
            get_mask_card_number("   ")



if __name__ == "__main__":
    pytest.main([__file__, "-v"])


