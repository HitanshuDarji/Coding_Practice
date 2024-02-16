"use client";
import { useState } from "react";
import Link from "next/link";
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";


const UpdateItemModal = ({item, closeUpdatePanel, reFetchData}) => {

    const [name, setName] = useState(item.Name);
    const [color, setColor] = useState(item.Color);
    const [flavor, setFlavor] = useState(item.Flavor);
    const [origin, setOrigin] = useState(item.Origin);

    const handleSubmit = async (event) => {
        
        event.preventDefault();
        const dataToSend = {
            "name": name,
            "color": color,
            "flavor": flavor,
            "origin": origin
        };

        try {
            await axios({
                method: 'put',
                url: `${BASE_URL}/coffees/update/${item.id}`,
                data: dataToSend
            })
        } catch (error) {
            console.log("Error in updating coffee item", error);
        } finally {
            await reFetchData();
            closeUpdatePanel(false);
        }
    };


    return (
        <div className="fixed flex inset-0 items-center justify-center pt-24 bg-opacity-80 z-50 bg-gray-900">
            <form className="bg-gray-900 w-1/3 p-8 mb-48 rounded-xl drop-shadow-2xl border-2 border-gray-700">
                <h1 className="pb-8 pt-2 font-bold text-3xl text-center">
                    Edit Item
                </h1>
                <div className="flex flex-row items-center justify-between pt-2 pb-2 font-bold">
                    <p>Coffee Name:</p>
                    <input onChange={(e) => {
                            setName(e.target.value)
                        }
                    } required type="text" value={name} className="rounded-md pt-2 pb-2 pr-4 pl-4 text-gray-900"/>
                </div>
                <div className="flex flex-row items-center justify-between pt-2 pb-2 font-bold">
                    <p>Coffee Color:</p>
                    <input onChange={(e) => {
                            setColor(e.target.value)
                        }
                    } type="text" value={color} className="rounded-md pt-2 pb-2 pr-4 pl-4 text-gray-900"/>
                </div>
                <div className="flex flex-row items-center justify-between pt-2 pb-2 font-bold">
                    <p>Coffee Flavor:</p>
                    <input onChange={(e) => {
                            setFlavor(e.target.value)
                        }
                    } type="text" value={flavor} className="rounded-md pt-2 pb-2 pr-4 pl-4 text-gray-900"/>
                </div>
                <div className="flex flex-row items-center justify-between pt-2 pb-2 font-bold">
                    <p>Coffee Origin:</p>
                    <input onChange={(e) => {
                            setOrigin(e.target.value)
                        }
                    } type="text" value={origin} className="rounded-md pt-2 pb-2 pr-4 pl-4 text-gray-900"/>
                </div>
                <div className="flex flex-row items-center justify-between pt-8 pb-2 font-bold">
                    <button onClick={() => {closeUpdatePanel(false)}} className="pt-2 pb-2 pr-4 pl-4 text-gray-100 bg-rose-800 rounded-full w-fit font-bold hover:bg-rose-900">
                        Close
                    </button>
                    <button onClick={handleSubmit} className="pt-2 pb-2 pr-4 pl-4 text-gray-900 bg-lime-500 rounded-full w-fit font-bold hover:bg-lime-600">Update</button>
                </div>
            </form>
        </div>
    );
}

export default UpdateItemModal;