import os
import services.services as ss

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    ss.app.run(host='0.0.0.0', port=port)
