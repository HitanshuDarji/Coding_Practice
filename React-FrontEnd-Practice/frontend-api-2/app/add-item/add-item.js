import Link from "next/link";

const AddItemModal = () => {
    return (
        <div className="flex flex-col items-center justify-center w-screen h-screen pt-24 bg-zinc-600">
            <form className="bg-gray-900 w-1/3 p-8 mb-48 rounded-xl drop-shadow-2xl">
                <h1 className="pb-8 pt-2 font-bold text-3xl text-center">
                    Add New Item
                </h1>
                <div className="flex flex-row items-center justify-between pt-2 pb-2 font-bold">
                    <p>Coffee ID:</p>
                    <input type="text" placeholder="Enter coffee ID" className="rounded-md pt-2 pb-2 pr-4 pl-4 text-gray-900"/>
                </div>
                <div className="flex flex-row items-center justify-between pt-2 pb-2 font-bold">
                    <p>Coffee Name:</p>
                    <input type="text" placeholder="Enter coffee name" className="rounded-md pt-2 pb-2 pr-4 pl-4 text-gray-900"/>
                </div>
                <div className="flex flex-row items-center justify-between pt-2 pb-2 font-bold">
                    <p>Coffee Color:</p>
                    <input type="text" placeholder="Enter coffee color" className="rounded-md pt-2 pb-2 pr-4 pl-4 text-gray-900"/>
                </div>
                <div className="flex flex-row items-center justify-between pt-2 pb-2 font-bold">
                    <p>Coffee Flavor:</p>
                    <input type="text" placeholder="Enter coffee flavor" className="rounded-md pt-2 pb-2 pr-4 pl-4 text-gray-900"/>
                </div>
                <div className="flex flex-row items-center justify-between pt-2 pb-2 font-bold">
                    <p>Coffee Origin:</p>
                    <input type="text" placeholder="Enter coffee origin" className="rounded-md pt-2 pb-2 pr-4 pl-4 text-gray-900"/>
                </div>
                <div className="flex flex-row items-center justify-between pt-8 pb-2 font-bold">
                    <button className="pt-2 pb-2 pr-4 pl-4 text-gray-100 bg-rose-800 rounded-full w-fit font-bold hover:bg-rose-900">
                        <Link href="./table-view">Cancel</Link>
                    </button>
                    <button className="pt-2 pb-2 pr-4 pl-4 text-gray-900 bg-lime-500 rounded-full w-fit font-bold hover:bg-lime-600">Add</button>
                </div>
            </form>
        </div>
    );
}

export default AddItemModal;