const API_BASE_URL = 'http://localhost:8000';

function navigateToTest(testRoute) {
    const url = `${API_BASE_URL}/${testRoute}`;
    
    // Можно использовать fetch для получения данных с бэкенда
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);
            // Здесь можно добавить логику обработки ответа
            // Например, перенаправление на страницу с тестом или отображение содержимого
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Произошла ошибка при загрузке теста. Пожалуйста, попробуйте позже.');
        });
}

async function sendMessage(message) {
    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        return data.response;
    } catch (error) {
        console.error('Error:', error);
        return 'Извините, произошла ошибка при обработке вашего сообщения.';
    }
}

// Экспортируем функцию для использования в других файлах
export { sendMessage }; 