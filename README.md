# AI Training Recommender System

A Flask-based AI system that recommends training programs for faculty members based on their performance metrics using Random Forest classification.

## 🚀 Live Demo

**API Endpoint:** `https://ai-training-recommender.onrender.com/recommend-training`

## 📋 Overview

This system analyzes faculty performance across 5 key areas and recommends appropriate training programs:

- **Subject Knowledge** (2.5-5.0)
- **Engagement** (2.5-5.0)  
- **Management** (2.5-5.0)
- **Preparedness** (2.5-5.0)
- **Professionalism** (2.5-5.0)

## 🎯 Available Training Recommendations

- Advanced Curriculum Design
- Classroom Management Workshop
- Engaging Students in Online Learning
- Research Writing and Publication
- Effective Assessment Strategies
- Integrating Technology in Teaching
- Stress Management and Faculty Wellness
- Improving Communication Skills
- Outcome-Based Education Seminar
- Time Management for Educators
- Innovative Teaching Strategies
- Building Empathy in the Classroom
- Using Rubrics Effectively
- Instructional Leadership Training
- Creating Inclusive Learning Environments
- Digital Pedagogy Workshop
- Emotional Intelligence for Educators
- Blended Learning Design
- Flipped Classroom Implementation

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **ML Model:** Random Forest Classifier (scikit-learn)
- **Model Storage:** joblib
- **CORS:** flask-cors
- **Web Server:** Gunicorn
- **Deployment:** Render.com

## 📁 Project Structure

```
ai-training-recommender/
├── application.py              # Main Flask application
├── train_model.py             # Model training script
├── generate_data_variations.py # Data generation utility
├── training_model.pkl         # Trained Random Forest model
├── training_data.csv          # Training dataset
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🔧 Installation & Setup

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-training-recommender.git
   cd ai-training-recommender
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python application.py
   ```

4. **Test locally:**
   API will be available at `http://localhost:5000/recommend-training`

### Deployment on Render

1. **Push to GitHub** (public repository)
2. **Connect to Render:**
   - Go to [render.com](https://render.com)
   - Create new Web Service
   - Connect GitHub repository
3. **Configure deployment:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn application:app`
   - **Plan:** Free
   - **Region:** Singapore (recommended for Asia-Pacific)

## 📡 API Usage

### Endpoint
```
POST https://ai-training-recommender.onrender.com/recommend-training
```

### Request Headers
```
Content-Type: application/json
```

### Request Body
```json
{
    "subject_knowledge": 3.5,
    "engagement": 4.0,
    "management": 3.0,
    "preparedness": 4.5,
    "professionalism": 3.8
}
```

### Response
```json
{
    "recommended_training": "Effective Assessment Strategies"
}
```

### Error Response
```json
{
    "error": "Error message here"
}
```

## 🧪 Testing Examples

### Using curl
```bash
curl -X POST https://ai-training-recommender.onrender.com/recommend-training \
  -H "Content-Type: application/json" \
  -d '{
    "subject_knowledge": 3.5,
    "engagement": 4.0,
    "management": 3.0,
    "preparedness": 4.5,
    "professionalism": 3.8
  }'
```

### Using Postman
1. Method: `POST`
2. URL: `https://ai-training-recommender.onrender.com/recommend-training`
3. Headers: `Content-Type: application/json`
4. Body: Raw JSON (see request body above)

### Using PHP (Proxy)
```php
<?php
header('Content-Type: application/json');

try {
    $input = json_encode(json_decode(file_get_contents('php://input'), true));

    $ch = curl_init('https://ai-training-recommender.onrender.com/recommend-training');
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $input);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);

    $response = curl_exec($ch);
    
    if (curl_errno($ch)) {
        http_response_code(500);
        echo json_encode(['error' => curl_error($ch)]);
    } else {
        echo $response;
    }

    curl_close($ch);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['error' => $e->getMessage()]);
}
?>
```

## 📊 Model Details

- **Algorithm:** Random Forest Classifier
- **Features:** 5 performance metrics (all numerical, scale 2.5-5.0)
- **Training Data:** 57 samples across 19 training categories
- **Model File:** `training_model.pkl` (included in repository)

## ⚠️ Render Free Tier Limitations

- **Usage:** 750 hours/month
- **Sleep Mode:** App sleeps after 15 minutes of inactivity
- **Cold Start:** ~30 seconds wake-up time
- **Resources:** 512MB RAM, 0.1 CPU

## 🔄 Model Retraining

To retrain the model with new data:

1. **Update training data:**
   ```bash
   python generate_data_variations.py
   ```

2. **Retrain model:**
   ```bash
   python train_model.py
   ```

3. **Redeploy to Render** (automatic via GitHub)

## 📝 Dependencies

```
Flask
flask-cors
scikit-learn
numpy
gunicorn
joblib
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Developer: Naskiiiieeeee

Created for faculty training recommendation system.

---

**Need help?** Check the logs on Render dashboard or create an issue in this repository.
