import { FaSearch } from "react-icons/fa";
import { useState } from "react";
import Link from "next/link";

const BASE_URL = "http://127.0.0.1:8000";

const SearchBar = ({setResults, toggleAddModal}) => {

    const [userInput, setUserInput] = useState("");

    const fetchData  = async (value) => {
        const response = await fetch(`${BASE_URL}/coffees`);
        const data = await response.json();
        const coffeeItems = Object.values(data.items);
        const results = coffeeItems.filter((item) => {
            return (
                value && item && item.Name && item.Name.toLowerCase().includes(value.toLowerCase()) ||
                value && item && item.Color && item.Color.toLowerCase().includes(value.toLowerCase()) ||
                value && item && item.Flavor && item.Flavor.toLowerCase().includes(value.toLowerCase()) ||
                value && item && item.Origin && item.Origin.toLowerCase().includes(value.toLowerCase())
            ); 
        });
        setResults(results);
    };

    const handleSearch = (value) => {
        setUserInput(value);
        fetchData(value);
    };

    return (
        <div className="flex flex-row items-center justify-between">
            <div className="flex flex-row items-center rounded-full w-full h-10 bg-gray-700 text-center mb-4 mr-2 pl-4 pr-4 drop-shadow-lg hover:bg-gray-800">
                <FaSearch className="text-lime-500"/>
                <input
                value={userInput}
                placeholder="Search"
                className="border-none bg-transparent w-full h-full ml-4 focus:outline-none"
                onChange={(e) => {handleSearch(e.target.value)}}
                />
            </div>
            <button onClick={() => {toggleAddModal(true)}} className="p-2 text-gray-900 bg-lime-500 rounded-full w-32 font-bold mb-4 drop-shadow-xl hover:bg-lime-600">
                Add New +
            </button>
        </div> 
    );
}

export default SearchBar;