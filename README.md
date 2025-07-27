# PDF Outline Extractor - Adobe Hackathon Round 1A

## 🚀 Run with Docker

```bash
docker build --platform linux/amd64 -t outline_extractor:latest .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none outline_extractor:latest
```

## 📄 Input/Output
- Place PDFs inside `/input`
- JSONs will be created in `/output`
