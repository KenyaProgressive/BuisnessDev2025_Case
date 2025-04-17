const API_BASE_URL = 'http://localhost:8000';

// Глобальный массив для хранения истории диалога
let chatHistory = [];

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

async function handleMessage() {
    const message = messageInput.value.trim();
    if (!message) return;

    // Отключаем кнопку и инпут на время отправки
    sendButton.disabled = true;
    messageInput.disabled = true;

    // Добавляем сообщение пользователя
    addMessage(message, true);
    
    // Очищаем поле ввода
    messageInput.value = '';

    try {
        const response = await fetch('/tests/test3/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: message })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Ответ от сервера:', data); // Оставляем важный лог для отладки
        addMessage(data.response, false);
    } catch (error) {
        console.error('Ошибка:', error); // Оставляем лог ошибок
        addMessage('Извините, произошла ошибка при обработке вашего сообщения.', false);
    } finally {
        // Включаем кнопку и инпут обратно
        sendButton.disabled = false;
        messageInput.disabled = false;
        messageInput.focus();
    }
}

// Добавляем обработчики событий
sendButton.addEventListener('click', handleMessage);
messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        handleMessage();
    }
});

// Функция для добавления сообщений в историю
function addToHistory(userMessage, aiResponse) {
    chatHistory.push({
        user_input: userMessage,
        ai_response: aiResponse,
        timestamp: new Date().toISOString()
    });
}

// Функция отправки всей истории при выходе
async function saveAndExit() {
    // Сохраняем историю в БД
    await fetch('/tests/test3/save_history', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ history: chatHistory })
    });
    
    // Возвращаемся на главную
    window.location.href = '/';
}

function addMessageToChat(type, message) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Экспортируем функцию для использования в других файлах
export { handleMessage }; 