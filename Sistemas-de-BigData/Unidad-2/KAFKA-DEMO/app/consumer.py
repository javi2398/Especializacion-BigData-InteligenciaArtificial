from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "demo",
    bootstrap_servers=["kafka:9093"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="grupo-demo",
)

print("Consumiendo mensajes de 'demo'...")
for msg in consumer:
    print(f"Recibido: {msg.value.decode('utf-8')}")