import threading
import asyncio
import random
from flask import Flask
from telethon import TelegramClient, events
import requests

# --- CONFIGURA AQUÍ TU API_ID y API_HASH ---
api_id = 14367814
api_hash = '2c219bbc33721773e7fc3e472a269f47'

client = TelegramClient('session_session', api_id, api_hash)

# Flask app para puerto abierto
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot funcionando"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

# ------------------- DATOS FALSOS --------------------
fake_passwords = [
    "p@$$w0rd123", "admin1234", "letmein!", "123456789", "trustno1",
    "hunter2", "correcthorsebatterystaple", "iloveyou123", "qwertyuiop"
]
fake_ips = [
    "192.168.1.42", "10.0.0.13", "172.16.254.1", "203.0.113.15", "198.51.100.23",
    "45.33.32.156", "178.62.193.19"
]
fake_locations = {
    "usa": ["New York, USA", "Los Angeles, USA", "Chicago, USA"],
    "germany": ["Berlin, Germany", "Munich, Germany", "Frankfurt, Germany"],
    "brazil": ["São Paulo, Brazil", "Rio de Janeiro, Brazil", "Brasília, Brazil"],
    "japan": ["Tokyo, Japan", "Osaka, Japan", "Kyoto, Japan"],
    "france": ["Paris, France", "Lyon, France", "Marseille, France"]
}
fake_ports = [22, 80, 443, 8080, 3306, 21, 25, 110, 995, 993]

fake_names = {
    "usa": ["John Doe", "Jane Smith", "Michael Johnson", "Emily Davis"],
    "germany": ["Hans Müller", "Anna Schmidt", "Peter Fischer", "Laura Becker"],
    "brazil": ["João Silva", "Maria Souza", "Carlos Oliveira", "Ana Pereira"],
    "japan": ["Takeshi Yamada", "Yuki Tanaka", "Haruto Saito", "Miyu Kobayashi"],
    "france": ["Jean Dupont", "Marie Martin", "Pierre Bernard", "Sophie Laurent"]
}

# ------------------- FUNCIONES GENERALES --------------------
def big_banner(text):
    banner = f"""
╔══════════════════════════════════════════════╗
║                                              ║
║     {text.center(40)}     ║
║                                              ║
╚══════════════════════════════════════════════╝
"""
    return banner

def progress_bar(progress, total=30):
    filled = int(progress / total * 100 // 3.33)
    bar = "█" * filled + "▒" * (30 - filled)
    percent = progress * 100 // total
    return f"[{bar}] {percent}%"

# ------------------- /hack --------------------
async def simulate_hack(event, target_username):
    me = await client.get_me()
    steps = [
        "INICIANDO ATAQUE DE ALTA INTENSIDAD",
        "ESCANEANDO PUERTOS ABIERTOS",
        "BRECHA DE SEGURIDAD ENCONTRADA",
        "INYECCIÓN DE CÓDIGO MALICIOSO",
        "DESCARGANDO ARCHIVOS SENSIBLES",
        "DESCIFRANDO CONTRASEÑAS",
        "ESTABLECIENDO PUERTA TRASERA",
        "EXFILTRANDO DATOS AL SERVIDOR",
        "CANCELANDO LOGS DE ACCESO",
        "COMPROMETIENDO SISTEMA DE AUTENTICACIÓN",
        "ACCESO COMPLETADO CON ÉXITO"
    ]

    progress_msg = await event.respond("```" + big_banner("COMIENZA EL ATAQUE") + "```", parse_mode='markdown')
    await asyncio.sleep(2)

    for step in steps:
        if "ESCANEANDO" in step:
            for port in fake_ports:
                bar = progress_bar(fake_ports.index(port)+1, len(fake_ports))
                await progress_msg.edit(f"```\n{step}\nPuerto {port} abierto\n{bar}\n```", parse_mode='markdown')
                await asyncio.sleep(random.uniform(0.8, 1.5))
        elif "DESCIFRANDO" in step:
            for prog in range(0, 31, 3):
                bar = progress_bar(prog)
                await progress_msg.edit(f"```\n{step}\n{bar}\n```", parse_mode='markdown')
                await asyncio.sleep(random.uniform(1.0, 1.7))
        else:
            await progress_msg.edit(f"```\n{step}\n```", parse_mode='markdown')
            await asyncio.sleep(random.uniform(1.2, 2.2))

    fake_password = random.choice(fake_passwords)
    fake_ip = random.choice(fake_ips)
    fake_location = random.choice(fake_locations["usa"])

    final_text = f"""
╔══════════════════════════════════════════════╗
║                                              ║
║           ACCESO AL USUARIO OBTENIDO         ║
║                                              ║
║  Usuario: {target_username.ljust(35)}║
║  ID de usuario: {me.id}{" "*(33-len(str(me.id)))}║
║  Contraseña (fake): {fake_password.ljust(28)}║
║  Última IP detectada: {fake_ip.ljust(27)}║
║  Ubicación estimada: {fake_location.ljust(27)}║
║                                              ║
╚══════════════════════════════════════════════╝

                    CREATED BY: @LooKsCrazy0
"""
    await progress_msg.edit(f"```{final_text}```", parse_mode='markdown')

@client.on(events.NewMessage(pattern=r'/hack (.+)'))
async def handler(event):
    target_username = event.pattern_match.group(1)
    await simulate_hack(event, target_username)

# ------------------- /fake --------------------
@client.on(events.NewMessage(pattern=r'/fake\s*(\w+)?'))
async def fake_data(event):
    country_key = event.pattern_match.group(1)
    if country_key:
        country_key = country_key.lower()
    else:
        country_key = "usa"

    if country_key not in fake_locations:
        await event.respond(f"País no soportado. Usa uno de: {', '.join(fake_locations.keys())}")
        return

    progress_msg = await event.respond("```\nGenerando datos falsos...\n[▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒] 0%\n```", parse_mode='markdown')

    for i in range(0, 31, 5):
        bar = progress_bar(i)
        await progress_msg.edit(f"```\nGenerando datos falsos...\n{bar}\n```", parse_mode='markdown')
        await asyncio.sleep(0.5)

    fake_name = random.choice(fake_names[country_key])
    fake_password = random.choice(fake_passwords)
    fake_ip = random.choice(fake_ips)
    fake_location = random.choice(fake_locations[country_key])
    fake_port = random.choice(fake_ports)

    message = f"""
╔════════════════════════════════════════╗
║         Datos Falsos Generados         ║
╠════════════════════════════════════════╣
║ Nombre: {fake_name.ljust(28)}║
║ Contraseña: {fake_password.ljust(24)}║
║ IP: {fake_ip.ljust(34)}║
║ Ubicación: {fake_location.ljust(27)}║
║ Puerto abierto: {str(fake_port).ljust(22)}║
╚════════════════════════════════════════╝

CREATED BY: @LooKsCrazy0
"""
    await progress_msg.edit(f"```{message}```", parse_mode='markdown')

# ------------------- /genbin --------------------
bin_prefixes = {
    "visa": ["4"],
    "mastercard": ["51", "52", "53", "54", "55"],
    "amex": ["34", "37"],
    "american": ["34", "37"]
}

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_sum = sum(digits[-1::-2])
    even_sum = 0
    for d in digits[-2::-2]:
        doubled = d * 2
        even_sum += sum(digits_of(doubled))
    return (odd_sum + even_sum) % 10

def calculate_luhn(partial_card):
    check_digit = luhn_checksum(int(partial_card) * 10)
    return (10 - check_digit) % 10

def generate_bin(card_type):
    if card_type not in bin_prefixes:
        return None
    prefix = random.choice(bin_prefixes[card_type])
    length = 15 if card_type in ["amex", "american"] else 16
    number = prefix
    while len(number) < (length - 1):
        number += str(random.randint(0,9))
    check_digit = calculate_luhn(number)
    number += str(check_digit)
    return number

@client.on(events.NewMessage(pattern=r'/genbin (.+)'))
async def genbin(event):
    card_type = event.pattern_match.group(1).lower()
    if card_type not in bin_prefixes:
        await event.respond("Tipo de tarjeta no soportado. Usa: visa, mastercard, amex, american")
        return

    progress_msg = await event.respond("Conectando al banco más cercano...\n[▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒] 0%", parse_mode='markdown')
    for i in range(0, 31, 5):
        bar = progress_bar(i)
        await progress_msg.edit(f"Conectando al banco más cercano...\n{bar}")
        await asyncio.sleep(0.5)

    bin_generated = generate_bin(card_type)
    message = f"""
╔════════════════════════════════════╗
║      BIN Generado para {card_type.capitalize()}      ║
╠════════════════════════════════════╣
║ Número: {bin_generated.ljust(27)}║
╚════════════════════════════════════╝

CREATED BY: @LooKsCrazy0
"""
    await progress_msg.edit(f"```{message}```", parse_mode='markdown')

# ------------------- /bin --------------------
@client.on(events.NewMessage(pattern=r'/bin (\d{6})'))
async def bin_info(event):
    bin_code = event.pattern_match.group(1)
    progress_msg = await event.respond("Consultando BIN...\n[▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒] 0%", parse_mode='markdown')

    for i in range(0, 31, 5):
        bar = progress_bar(i)
        await progress_msg.edit(f"Consultando BIN...\n{bar}")
        await asyncio.sleep(0.5)

    try:
        url = f"https://lookup.binlist.net/{bin_code}"
        headers = {'Accept-Version': '3'}
        response = requests.get(url, headers=headers)
        data = response.json()

        tipo = data.get("type", "Desconocido").capitalize()
        marca = data.get("scheme", "Desconocido").capitalize()
        prepaid = "Sí" if data.get("prepaid", False) else "No"
        banco = data.get("bank", {}).get("name", "Desconocido")
        ciudad = data.get("bank", {}).get("city", "N/A")
        telefono = data.get("bank", {}).get("phone", "N/A")
        pagina = data.get("bank", {}).get("url", "N/A")
        pais = data.get("country", {}).get("name", "Desconocido")

        message = f"""
╔════════════════════════════════════╗
║       Información del BIN {bin_code}       ║
╠════════════════════════════════════╣
║ Tipo: {tipo.ljust(28)}║
║ Marca: {marca.ljust(28)}║
║ Es prepago: {prepaid.ljust(20)}║
║ Esquema: {marca.ljust(28)}║
║ País: {pais.ljust(28)}║
║ Banco: {banco.ljust(28)}║
║ Ciudad Banco: {ciudad.ljust(28)}║
║ Teléfono Banco: {telefono.ljust(28)}║
║ Página Banco: {pagina.ljust(28)}║
╚════════════════════════════════════╝

CREATED BY: @LooKsCrazy0
"""
        await progress_msg.edit(f"```{message}```", parse_mode='markdown')

    except Exception as e:
        await progress_msg.edit(f"Error al consultar BIN: {str(e)}")

# ------------------- /randomquote --------------------
motivational_quotes = [
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "No sueñes tu vida, vive tu sueño.",
    "La disciplina es el puente entre metas y logros.",
    "El único lugar donde el éxito viene antes que el trabajo es en el diccionario.",
    "No importa lo lento que avances, siempre y cuando no te detengas.",
    "Cada día es una nueva oportunidad para cambiar tu vida.",
    "La clave del éxito está en enfocarte en metas, no en obstáculos.",
    "El fracaso es solo la oportunidad para comenzar de nuevo con más experiencia.",
    "No cuentes los días, haz que los días cuenten.",
    "La motivación te impulsa, el hábito te mantiene en marcha."
]

used_quotes = set()

@client.on(events.NewMessage(pattern=r'/randomquote'))
async def random_quote(event):
    global used_quotes
    progress_msg = await event.respond("Cargando frase...\n[▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒] 0%", parse_mode='markdown')

    for i in range(0, 31, 5):
        bar = progress_bar(i)
        await progress_msg.edit(f"Cargando frase...\n{bar}")
        await asyncio.sleep(0.5)

    if len(used_quotes) == len(motivational_quotes):
        used_quotes.clear()  # Reiniciar cuando se usen todas

    remaining_quotes = [q for q in motivational_quotes if q not in used_quotes]
    quote = random.choice(remaining_quotes)
    used_quotes.add(quote)

    await progress_msg.edit(f"💡 *Frase motivacional:*\n\n_{quote}_\n\n_CREADO POR: @LooKsCrazy0_", parse_mode='markdown')

# ------------------- /cgen --------------------
@client.on(events.NewMessage(pattern=r'/cgen (\d{6,8})(?: (\d+))?(?: (\d{2}/\d{2}))?(?: (\d{3}))?'))
async def cgen(event):
    bin_input = event.pattern_match.group(1)
    cantidad = int(event.pattern_match.group(2)) if event.pattern_match.group(2) else 1
    cantidad = min(cantidad, 10)  # máximo 10 tarjetas
    exp_date = event.pattern_match.group(3)
    cvv_input = event.pattern_match.group(4)

    progress_msg = await event.respond("Generando tarjetas...\n[▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒] 0%", parse_mode='markdown')

    for i in range(0, 31, 5):
        bar = progress_bar(i)
        await progress_msg.edit(f"Generando tarjetas...\n{bar}")
        await asyncio.sleep(0.5)

    tarjetas = []
    for _ in range(cantidad):
        length = 16
        card_number = bin_input
        while len(card_number) < (length - 1):
            card_number += str(random.randint(0,9))
        check_digit = calculate_luhn(card_number)
        card_number += str(check_digit)
        fecha = exp_date if exp_date else f"{random.randint(1,12):02d}/{random.randint(24,29)}"
        cvv = cvv_input if cvv_input else f"{random.randint(100,999)}"
        tarjetas.append((card_number, fecha, cvv))

    msg = "╔════════════════════════════════════╗\n║         Tarjetas Generadas         ║\n╠════════════════════════════════════╣\n"
    for t in tarjetas:
        msg += f"║ Número: {t[0]}          ║\n║ Fecha Exp: {t[1]}                   ║\n║ CVV: {t[2]}                           ║\n╠════════════════════════════════════╣\n"
    msg += "╚════════════════════════════════════╝\n\nCREATED BY: @LooKsCrazy0"
    await progress_msg.edit(f"```{msg}```", parse_mode='markdown')

# ------------------- /attack --------------------
@client.on(events.NewMessage(pattern=r'/attack (@\w+) "(.+)" (\d+)'))
async def attack_user(event):
    target = event.pattern_match.group(1)
    message = event.pattern_match.group(2)
    count = int(event.pattern_match.group(3))
    if count > 50:
        count = 50

    progress_msg = await event.respond("Iniciando ataque...\n[▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒] 0%", parse_mode='markdown')

    for i in range(0, 31, 5):
        bar = progress_bar(i)
        await progress_msg.edit(f"Iniciando ataque a {target}...\n{bar}")
        await asyncio.sleep(0.5)

    for i in range(1, count + 1):
        await client.send_message(target, message)
        bar = progress_bar(int(i / count * 30))
        await progress_msg.edit(f"Enviando mensajes a {target}...\n{bar} ({i}/{count})")
        await asyncio.sleep(1)

    await progress_msg.edit(f"✅ Ataque completado. Se enviaron {count} mensajes a {target}.")

# ------------------- INICIO DEL BOT --------------------
async def main():
    print("Sesión iniciada. Esperando comandos...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    asyncio.run(main())
