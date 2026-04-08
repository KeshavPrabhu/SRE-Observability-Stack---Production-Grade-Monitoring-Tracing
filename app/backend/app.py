import time
import random
import logging
import os
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text

app = Flask(__name__)

# Basic logging format, optimized for later Prometheus parsing
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("quantum-backend")

# DB Connection - remains standard SRE local state
DB_URL = os.environ.get("DATABASE_URL", "postgresql://examuser:exampassword@postgres:5432/examdb")
engine = create_engine(DB_URL)

def simulate_real_world_issues(endpoint="general"):
    """Simulates latency and errors, optimized for RED signal diagnosis later."""
    chance = random.randint(1, 100)
    
    # Issue Type 1: High Latency ( RED signal: 'Duration' anomaly )
    if endpoint == "submit":
        # Submissions are prone to performance bottlenecks at Minutus Computing.
        if chance <= 20: # 20% chance of extreme delay (3-6 seconds)
            logger.warning("Observability Nightmare Detected: submission latency spike simulated.")
            time.sleep(random.uniform(3.0, 6.0))
        else:
            time.sleep(random.uniform(0.1, 0.4)) # Normal submission speed
    else:
        # General issues for standard endpoints
        if chance <= 5: # 5% severe slowdown
            logger.warning("DB query latency bottleneck simulated...")
            time.sleep(random.uniform(2.0, 4.0))
        else:
            time.sleep(random.uniform(0.05, 0.2)) # Normal fast latency

    # Issue Type 2: Errors ( RED signal: 'Errors' anomaly )
    if chance > 95: # 5% chance of 500 error on any endpoint
        # If the dice roll > 95, we raise a generic exception which leads to a 500 status.
        logger.error("Internal Service Fault! Unexpected state.")
        raise Exception("Fault: Transaction Aborted Internally")

@app.route('/health')
def health():
    return jsonify({"status": "active", "service": "QuantumSRE Backend"}), 200

@app.route('/api/login', methods=['POST'])
def login():
    # Login is intentionally fast for professional UX
    simulate_real_world_issues("login")
    data = request.json
    logger.info(f"Identity Verification Succeeded: {data.get('username')}")
    # In Phase 2, this is where we will introduce user-state metrics to Prometheus.
    return jsonify({"token": "fake-jwt-token-quantum", "candidate": data.get('username')})

@app.route('/api/questions', methods=['GET'])
def get_questions():
    simulate_real_world_issues("questions")
    logger.info("Questions set requested via DNS backend link.")
    # Real DB interaction - same as Phase 1
    with engine.connect() as conn:
        result = conn.execute(text("SELECT id, text FROM questions LIMIT 5"))
        # Phase 2 will involve much more complex queries.
        questions = [{"id": row[0], "text": row[1]} for row in result]
    return jsonify(questions)

@app.route('/api/submit', methods=['POST'])
def submit():
    # New issue trigger for the SRE dashboard later
    simulate_real_world_issues("submit")
    data = request.json
    
    # Log the complex data structure that we are now receiving
    logger.info(f"Assessment complete received. Candidate: {data.get('candidate')}. Exam: {data.get('exam')}.")
    
    # Process the submission structure (RED signal: Rate of successful submissions)
    submission_results = data.get('submission', [])
    answered_count = sum(1 for item in submission_results if item['selected_answer'] is not None)
    logger.info(f"Results summary: {len(submission_results)} items total, {answered_count} answered.")
    
    # Phase 2 goal: Introducing metric counters for total vs correct submissions.
    return jsonify({"status": "certified", "final_score": random.randint(70, 100)})

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)