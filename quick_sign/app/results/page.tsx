'use client'
import React, {useEffect} from 'react';
import Link from 'next/link';
import axios from 'axios';
import {useRouter} from 'next/navigation';
import {func} from 'three/examples/jsm/nodes/Nodes.js';

axios.defaults.baseURL = 'http://127.0.0.1:8000';

const Result = () => {
    const univ = JSON.parse(localStorage.getItem("universities")) || [];
    const router = useRouter();
    const checkStorage = () => {
        if (univ.length === 0) {
            router.push("/panel")
        }
    }

    useEffect(() => {
        checkStorage();
    }, );


    return (
        <div className="min-h-screen flex items-center justify-center bg-white-100">
            <div className="bg-gray-300 rounded-lg shadow p-10 w-96 text-black">
                <div className="flex items-center space-x-2 mt-2">
                    <h2>Your best match is:</h2>
                    <ul>
                        {univ.map((element: any, index: any) => (
                            <li key={index}>{element}</li>
                        ))}
                    </ul>
                    <p>You are not satisfied?</p>
                    <Link href="/panel" passHref>
                        <button
                            className="mt-4 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-md">Try
                            Again!
                        </button>
                    </Link>
                </div>
            </div>
        </div>
    )

};

export default Result;