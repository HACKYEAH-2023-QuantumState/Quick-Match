'use client'
import React, {useState, useEffect} from 'react';
import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:8000';

function Survey() {
    const [userResponse, setUserResponse] = useState(0);
    const [question, setQuestion] = useState('');
    const [questionId, setQuestionId] = useState(0);
    const [error, setError] = useState(null);
    const [answers, setAnswers] = useState<{ [key: string]: number }>({});

    useEffect(() => {
        fetchFirstQuestion();
    }, []);

    const addAnswer = () => {
        if (question) {
            setAnswers(prev => ({
                ...prev,
                [questionId.toString()]: userResponse
            }));
        }
    };

    const fetchFirstQuestion = async () => {
        try {
            const response = await axios.post('/survey/', answers);
            const questionResponse = response.data.question;
            setQuestionId(questionResponse.questionId);
            setQuestion(questionResponse.questionText);
        } catch (error) {
            console.error('Error fetching question:', error);
            setError('Failed to load the question. Please try again later.');
        }
    };


    const sendAnswer = async () => {
        try {
            const temp = {...answers, [questionId.toString()]: userResponse}
            addAnswer();
            const response = await axios.post('/survey/', temp);
            const questionResponse = response.data.question;
            setQuestionId(questionResponse.questionId);
            setQuestion(questionResponse.questionText);
        } catch (error) {
            console.error('Error fetching question:', error);
            setError('Failed to load the question. Please try again later.');
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-100">
            <div className="bg-gray-300 rounded-lg shadow p-10 w-96">
                {error ? (
                    <p className="text-red-600">{error}</p>
                ) : (
                    <div>
                        <p className="text-black text-xl font-semibold">{question}</p>
                        <div className="flex items-center space-x-2 mt-2">
                            <input
                                type="range"
                                min="-2"
                                max="2"
                                step="1"
                                defaultValue="0"
                                className="w-48"
                                onChange={(e) => setUserResponse(parseInt(e.target.value))}
                            />
                            <span className="text-gray-600">
                {['Rawly Not', 'Rather Not', 'I Do Not Know', 'Rather Yes', 'Rawly Yes'][userResponse + 2]}
              </span>
                        </div>
                    </div>
                )}
                <button
                    onClick={sendAnswer}
                    className="mt-4 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-md"
                >
                    Next
                </button>
            </div>
        </div>
    );
}

export default Survey;
