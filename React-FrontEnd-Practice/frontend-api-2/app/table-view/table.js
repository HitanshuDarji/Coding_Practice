"use client";

import { useEffect, useState } from "react"
import SearchBar from "./search-bar";
import Modal from "./modal";
import AddItemModal from "../add-item/add-item";

const BASE_URL = "http://127.0.0.1:8000";

const Table = () => {
    const [data, setData] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [results, setResults] = useState([]);
    const [showModal, setShowModal] = useState(false);
    const [cid, setCid] = useState(0);

    useEffect(() => {
        const fetchData = async () => {
            setIsLoading(true);
            const response = await fetch(`${BASE_URL}/coffees`);
            const data = await response.json();
            const coffeeItems = Object.values(data.items);
            setData(coffeeItems);
            setIsLoading(false);
        }

        fetchData()

    }, []);

    const pageReloader = (argument) => {
        window.location.reload(argument)
    }

    return (
            <div className="text-gray-100 flex w-screen h-screen flex-col items-center bg-gray-900">
                {showModal && <Modal closeModal={setShowModal} cid={cid} pageReload={pageReloader}/>}
                {isLoading && <div>Loading...</div>}
                {!showModal && <div className="pt-24">
                    <h1 className=" text-4xl font-bold text-left p-4 w-1/2">Table View</h1>
                    <SearchBar setResults={setResults}/>
                        <div>
                            <table className="table-fixed bg-gray-900">
                                <thead>
                                    <tr>
                                        <th className="text-left p-4 bg-gray-700 rounded-tl-xl">Name</th>
                                        <th className="text-left p-4 bg-gray-700">Color</th>
                                        <th className="text-left p-4 bg-gray-700">Flavor</th>
                                        <th className="text-left p-4 bg-gray-700">Origin</th>
                                        <th className="text-center pt-4 pb-4 pr-4 pl-6 bg-gray-700 text-lime-500 rounded-tr-xl">Actions</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {results.length ? (results.map((item) => {
                                        return (
                                            <tr key={item.id} className="border-t-2 border-gray-700">
                                                <td className="p-4">{item.Name}</td>
                                                <td className="p-4">{item.Color}</td>
                                                <td className="p-4">{item.Flavor}</td>
                                                <td className="p-4">{item.Origin}</td>
                                                <td className="p-4">
                                                    <button className="p-2 mr-1 ml-1 text-gray-900 bg-lime-500 rounded-full w-24 font-bold hover:bg-lime-600">Edit</button>
                                                    <button onClick={() => {setShowModal(true); setCid(item.ud);}} className="p-2 mr-1 ml-1 text-white bg-rose-800 rounded-full w-24 font-bold hover:bg-rose-900">Remove</button>
                                                </td>
                                            </tr>
                                        );})) : (
                                        data.map((item) => {
                                            return (
                                                <tr key={item.id} className="border-t-2 border-gray-700">
                                                    <td className="p-4">{item.Name}</td>
                                                    <td className="p-4">{item.Color}</td>
                                                    <td className="p-4">{item.Flavor}</td>
                                                    <td className="p-4">{item.Origin}</td>
                                                    <td className="p-4">
                                                        <button className="p-2 mr-1 ml-1 text-gray-900 bg-lime-500 rounded-full w-24 font-bold hover:bg-lime-600">Edit</button>
                                                        <button onClick={() => {setShowModal(true); setCid(item.id);}} className="p-2 mr-1 ml-1 text-white bg-rose-800 rounded-full w-24 font-bold hover:bg-rose-900">Remove</button>
                                                    </td>
                                                </tr>
                                            );
                                        })
                                    )}
                                </tbody>
                            </table>
                        </div>
                </div>}
            </div>
    );
}
export default Table;