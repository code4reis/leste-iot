function updateSpeedometer(speed, elementId) {
    const needle = document.getElementById(elementId);
    const maxSpeed = 1000; // Ajuste o máximo para o velocímetro, por exemplo, 1000 Mbps
    const angle = Math.min(speed / maxSpeed * 180, 180); // Calcula o ângulo da agulha
    needle.style.transform = `rotate(${angle - 90}deg)`; // Ajusta o ângulo para começar do lado esquerdo
}

async function startSpeedTest() {
    const agentUrl = 'http://192.168.128.57:5000'; // URL do agente
    const button = document.getElementById('startButton');
    button.textContent = 'Em execução';
    button.disabled = true; // Desativa o botão

    try {
        const response = await fetch(`${agentUrl}/start_speedtest`, { method: 'GET' });
        const data = await response.json();

        if (response.ok && data.download_speed_mbps) {
            document.getElementById("download_speed").textContent = Math.round(data.download_speed_mbps);
            updateSpeedometer(Math.round(data.download_speed_mbps), "needle");
            document.getElementById("upload_speed").textContent = Math.round(data.upload_speed_mbps);
            document.getElementById("ping_result").textContent = data.ping_ms;
            document.getElementById("server_result").textContent = data.server.sponsor;

            // Enviar dados para o servidor Flask
            await fetch(`${agentUrl}/save_speedteste`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    download_speed_mbps: Math.floor(data.download_speed_mbps),  // Exemplo de conversão para número
                    upload_speed_mbps: Math.floor(data.upload_speed_mbps),      // Exemplo de conversão para número
                    ping_ms: Math.floor(data.ping_ms),                          // Convertendo para inteiro
                    server: data.server.sponsor.toString()                      // Convertendo para string
                })
            });
        } else if (data.error) {
            console.error(`Erro: ${data.error}`);
        } else {
            console.log('Nenhum dado de velocidade foi retornado.');
        }

    } catch (error) {
        console.error('Erro ao buscar velocidade:', error);
    }

    button.textContent = 'Iniciar Teste de Velocidade';
    button.disabled = false; // Reativa o botão
}

document.getElementById('startButton').addEventListener('click', startSpeedTest);
