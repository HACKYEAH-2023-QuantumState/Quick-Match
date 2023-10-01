'use client'
import React from 'react';
import Link from 'next/link';

const Result = () => {
    return(
        <div className="min-h-screen flex items-center justify-center bg-white-100">
        <div className="bg-gray-300 rounded-lg shadow p-10 w-96 text-black">
            <div className="flex items-center space-x-2 mt-2">
                <h2>Your best match is:</h2>
                <h1 className='size-100'>Phold</h1>
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