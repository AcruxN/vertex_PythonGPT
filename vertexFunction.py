import vertexai
import logging
from vertexai.generative_models import GenerativeModel, Part

# Logging
logger = logging.getLogger('vertexLogger')
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('vertexCall.log')
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# Vertex Function
def vertexCall(chatInput: str) -> str:
    vertexai.init(project="google_cloud_platform_project_name")
    multimodal_model = GenerativeModel(model_name="gemini-1.0-pro-vision-001")
    response = multimodal_model.generate_content(
        [
            chatInput,
        ]
    )
    print(response)
    print(response.text)
    logger.info(f"chatInput: {chatInput}")
    logger.info(f"response: {response.text}")
    return response.text