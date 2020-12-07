import logging

for i in range(10):
    ergebnis = i * 2
    print(ergebnis)


logging.basicConfig(level=logging.INFO)
logging.warning("Hallo Welt")
logging.info("Hallo Info")
