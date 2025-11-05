from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers=["kafka:9093"])
topic = "demo"

for i in range(1, 6):
    msg = f"mensaje-{i}".encode("utf-8")
    producer.send(topic, msg)
    print(f"Enviado: {msg.decode()}")
    time.sleep(0.5)

producer.flush()
producer.close()