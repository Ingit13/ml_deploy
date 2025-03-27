{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5aab13ff-4a67-42f8-b7c3-f91306c363f5",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2146833899.py, line 30)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[2], line 30\u001b[1;36m\u001b[0m\n\u001b[1;33m    predictive system.py\u001b[0m\n\u001b[1;37m               ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# -*- coding: utf-8 -*-\n",
    "\"\"\"\n",
    "Spyder Editor\n",
    "\n",
    "This is a temporary script file.\n",
    "\"\"\"\n",
    "\n",
    "import numpy as np\n",
    "import pickle\n",
    "\n",
    "# loading the saved model\n",
    "loaded_model = pickle.load(open('C:/Users/91936/Downloads/diabetes project/trained_model.sav', 'rb'))\n",
    "\n",
    "\n",
    "input_data = (5,166,72,19,175,25.8,0.587,51)\n",
    "\n",
    "# changing the input_data to numpy array\n",
    "input_data_as_numpy_array = np.asarray(input_data)\n",
    "\n",
    "# reshape the array as we are predicting for one instance\n",
    "input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)\n",
    "\n",
    "prediction = loaded_model.predict(input_data_reshaped)\n",
    "print(prediction)\n",
    "\n",
    "if (prediction[0] == 0):\n",
    "  print('The person is not diabetic')\n",
    "else:\n",
    "  print('The person is diabetic')\n",
    "predictive system.py\n",
    "Displaying predictive system.py."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8ba56ef9-92e5-4291-9a97-eb16eec008ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1]\n",
      "The person is diabetic\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\91936\\anaconda3\\Lib\\site-packages\\sklearn\\base.py:376: InconsistentVersionWarning: Trying to unpickle estimator SVC from version 1.6.1 when using version 1.4.2. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:\n",
      "https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations\n",
      "  warnings.warn(\n",
      "C:\\Users\\91936\\anaconda3\\Lib\\site-packages\\sklearn\\base.py:493: UserWarning: X does not have valid feature names, but SVC was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pickle\n",
    "\n",
    "# loading the saved model\n",
    "loaded_model = pickle.load(open('C:/Users/91936/Downloads/diabetes project/trained_model.sav', 'rb'))\n",
    "\n",
    "# input data for prediction\n",
    "input_data = (5,166,72,19,175,25.8,0.587,51)\n",
    "\n",
    "# changing the input_data to numpy array\n",
    "input_data_as_numpy_array = np.asarray(input_data)\n",
    "\n",
    "# reshape the array as we are predicting for one instance\n",
    "input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)\n",
    "\n",
    "# making the prediction\n",
    "prediction = loaded_model.predict(input_data_reshaped)\n",
    "\n",
    "# print the prediction result\n",
    "print(prediction)\n",
    "\n",
    "# conditionally print the result based on the prediction\n",
    "if prediction[0] == 0:\n",
    "    print('The person is not diabetic')\n",
    "else:\n",
    "    print('The person is diabetic')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a6cec2a6-5a53-4697-99c7-c42b93bb0a26",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
