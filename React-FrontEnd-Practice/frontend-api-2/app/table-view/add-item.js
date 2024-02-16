"use client";
import { useState } from "react";
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";


const AddItemModal = ({toggleAddModal, reFetchData}) => {

    const [name, setName] = useState("");
    const [color, setColor] = useState("");
    const [flavor, setFlavor] = useState("");
    const [origin, setOrigin] = useState("");

    const handleSubmit = async (event) => {

        event.preventDefault();
        const dataToSend = {
            name: name,
            color: color,
            flavor: flavor,
            origin: origin
        };

        try {
            await axios({
                method: 'post',
                url: `${BASE_URL}/coffees/add`,
                data: dataToSend
            })
        } catch (error) {
            console.log(error);
        } finally {
            await reFetchData();
            toggleAddModal(false);
        }

    }


    return (
        <div className="fixed inset-0 flex items-center justify-center pt-24 bg-gray-900 bg-opacity-80 z-50">
            <form onSubmit={handleSubmit} className="bg-gray-900 w-1/3 p-8 mb-48 rounded-xl drop-shadow-2xl border-2 border-gray-700">
                <h1 className="pb-8 pt-2 font-bold text-3xl text-center">
                    Add New Item
                </h1>
                <div className="flex flex-row items-center justify-between pt-2 pb-2 font-bold">
                    <p>Coffee Name:</p>
                    <input required onChange={(e) => setName(e.target.value)} type="text" placeholder="Enter coffee name" className="rounded-md pt-2 pb-2 pr-4 pl-4 text-gray-900"/>
                </div>
                <div className="flex flex-row items-center justify-between pt-2 pb-2 font-bold">
                    <p>Coffee Color:</p>
                    <input onChange={(e) => setColor(e.target.value)} type="text" placeholder="Enter coffee color" className="rounded-md pt-2 pb-2 pr-4 pl-4 text-gray-900"/>
                </div>
                <div className="flex flex-row items-center justify-between pt-2 pb-2 font-bold">
                    <p>Coffee Flavor:</p>
                    <input onChange={(e) => setFlavor(e.target.value)} type="text" placeholder="Enter coffee flavor" className="rounded-md pt-2 pb-2 pr-4 pl-4 text-gray-900"/>
                </div>
                <div className="flex flex-row items-center justify-between pt-2 pb-2 font-bold">
                    <p>Coffee Origin:</p>
                    <input onChange={(e) => setOrigin(e.target.value)} type="text" placeholder="Enter coffee origin" className="rounded-md pt-2 pb-2 pr-4 pl-4 text-gray-900"/>
                </div>
                <div className="flex flex-row items-center justify-between pt-8 pb-2 font-bold">
                    <button onClick={() => {toggleAddModal(false)}} className="pt-2 pb-2 pr-4 pl-4 text-gray-100 bg-rose-800 rounded-full w-fit font-bold hover:bg-rose-900">
                        Close
                    </button>
                    <button type="submit" className="pt-2 pb-2 pr-4 pl-4 text-gray-900 bg-lime-500 rounded-full w-fit font-bold hover:bg-lime-600">Add</button>
                </div>
            </form>
        </div>
    );
}

export default AddItemModal;