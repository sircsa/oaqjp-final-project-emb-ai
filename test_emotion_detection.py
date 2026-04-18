from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]
        for text, expected_label in test_cases:
            with self.subTest(text=text):
                result = emotion_detector(text)
                self.assertEqual(result['label'], expected_label)

if __name__ == '__main__':
    unittest.main()