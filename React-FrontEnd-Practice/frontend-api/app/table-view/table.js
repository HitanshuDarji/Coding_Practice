"use client";

import { useEffect, useState } from "react"

const BASE_URL = "http://127.0.0.1:8000";

const Table = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData  = async () => {
            const response = await fetch(`${BASE_URL}/coffees`);
            const data = await response.json();
            const coffeeItems = Object.values(data.items);
            setData(coffeeItems);
        }

        fetchData()

    }, []);

    return (
        <div>
            <h1>Fetching Data In React</h1>
                <table className="table-fixed border border-sky-300 mt-4 ml-4 rounded-xl">
                    <thead>
                        <tr className="border border-sky-300">
                            <th>Name</th>
                            <th>Color</th>
                            <th>Flavor</th>
                            <th>Origin</th>
                        </tr>
                    </thead>
                    <tbody>
                        {data.map((item) => {
                            return (
                                <tr className="p-2 border border-sky-300">
                                    <td className="p-2">{item.Name}</td>
                                    <td className="p-2">{item.Color}</td>
                                    <td className="p-2">{item.Flavor}</td>
                                    <td className="p-2">{item.Origin}</td>
                                </tr>
                            );
                        })}
                    </tbody>
                </table>
        </div>
    );
}

export default Table;