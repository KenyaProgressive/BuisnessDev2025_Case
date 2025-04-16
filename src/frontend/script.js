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