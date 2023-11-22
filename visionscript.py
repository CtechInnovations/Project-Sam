import cv2
import openai

cap = cv2.VideoCapture(0)

openai.api_key = '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' 

while True:

	ret, frame = cap.read()
	response = openai.Completion.create(
		engine="davinci",
		prompt="Describe the objects in this image: '{}'",
		max_tokens=100
	)
	description = response.choices[0].text.strip()
	
	cv2.putText(frame, description, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
	cv2.imshow('Image', frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
cap.release()
cv2.destroyAllWindows()