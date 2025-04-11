# Virtual Telecaller

## Overview
A virtual AI telecaller system that combines voice calls with AI-powered responses. The system uses speech recognition to transcribe calls, processes them through a fine-tuned LLM, and delivers natural-sounding responses.

## Features
- Real-time voice calls using Zego Express SDK
- Speech-to-text transcription
- AI response generation using fined tuned Meta-Llama/Llama-3.2-3B-Instruct on the dataset Bitext-media-llm-chatbot-training-dataset 
- Text-to-speech conversion for spoken responses
- Interactive chat interface alternative

## Architecture
- **Frontend**: React application with voice and chat interfaces
- **Backend**: Flask server handling API requests and file operations
- **Model Hosting**: Fine-tuned Llama model running in Kaggle notebook
- **Data Transfer**: Google Drive as middleware for file exchange

## Workflow
1. User initiates a call in the frontend
2. Speech recognition converts spoken words to text
3. Text is sent to Flask backend
4. Backend uploads text to Google Drive
5. Kaggle notebook retrieves the query, processes via LLM
6. Response is saved back to Google Drive
7. Backend fetches and forwards response to frontend
8. Frontend displays and speaks the response
9. Requirement of google drive bridge as training locally can be computationally expensive.
10. Another functionality of chatbot which can give responses in written form after manually typing your queries.

## Tech Stack
- React.js
- Zego Express Engine WebRTC
- Flask + CORS
- Google Drive API
- Meta-Llama/Llama-3.2-3B-Instruct (fine-tuned)

### Prerequisites
- Node.js and npm
- Python 3.13.2
- Google Drive API credentials
- Zego API credentials

### Installation
```bash
# Clone repository
git clone [repository-url]
cd telecaller
```

# Frontend setup
```bash
cd frontend
npm install
```
# Backend setup
```bash
cd ../backend
pip install -r requirements.txt
```

### Configuration
1. Update Zego credentials in `ZegoCall.js`:
   ```bash
   const APP_ID = [your-app-id]
   const APP_SIGN = [your-app-sign]
   const TOKEN=[zego_call_token]
   ```

2. Configure Google Drive access in `app.py`:
   ```bash python
   SERVICE_ACCOUNT_FILE = 'path/to/credentials.json'
   YOUR_EMAIL = 'your-email@example.com'
   FOLDER_ID = 'your-drive-folder-id'
   ```

3. Set up model endpoints:
   ```bash python
   endpoint = "your-model-endpoint"
   token = "your-api-key"
   ```

### Running the Application
```bash
# Start backend
cd backend
python final.py
```
# Start frontend (in a new terminal)
```bash
cd frontend
npm run dev
npm start
```

## Usage
1. Open the application in your browser
2. Click "Start Call" to begin a voice conversation
3. Speak naturally - your speech will be transcribed
4. The AI will process your query and respond both visually and audibly
5. Alternatively, use the chat interface by clicking "Open Chatbot"

## Known Limitations
- Response time depends on network conditions and Drive sync speed
- Speech recognition accuracy varies by environment and accent
- Model responses limited by training data scope

## Future Improvements
- Direct API communication instead of Drive middleware with availabilty of more computational resources.
- Enhanced error handling and recovery
- User authentication and personalization
- Expanded training dataset for better responses
