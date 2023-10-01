'use client'
import React from 'react';
import Link from 'next/link';
import axios from 'axios';
import { useRouter } from 'next/navigation';
import { func } from 'three/examples/jsm/nodes/Nodes.js';

axios.defaults.baseURL = 'http://127.0.0.1:8000';

const univ = localStorage.getItem('universities', JSON.stringify(unis));



const Result = () => {
    const router = useRouter();
    const getAnswer = ()=> {
        if(univ){
        univ.forEach(element => {
            return <h1>element</h1>
        });
        }else{
            router.push("/panel")
        }
    }
    return(
        <div className="min-h-screen flex items-center justify-center bg-white-100">
        <div className="bg-gray-300 rounded-lg shadow p-10 w-96 text-black">
            <div className="flex items-center space-x-2 mt-2">
                <h2>Your best match is:</h2>
                {getAnswer}
                <p>You are not satisfied?</p>
                <Link href="/panel" passHref>
                <button className="mt-4 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-md">Try Again!</button>
                </Link>
            </div>
        </div>
    </div>
    )

};

export default Result;