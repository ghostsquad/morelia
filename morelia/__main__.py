import traceback
import sys
import logging
from morelia import main

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    try:
        logging.basicConfig(
            stream=sys.stdout,
            level=logging.INFO,
            format="%(asctime)s [%(levelname)8s] %(message)s")
        main(sys.argv[1:])
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
