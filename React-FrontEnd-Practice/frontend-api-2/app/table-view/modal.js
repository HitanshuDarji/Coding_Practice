import React from 'react'

const BASE_URL = "http://127.0.0.1:8000";


function Modal({closeModal, cid, reFetchData}) {

    const deleteItem = async () => {
        await fetch(`${BASE_URL}/coffees/delete/${cid}`, {method:'DELETE'});
        await reFetchData()
        closeModal(false);
    }

    return (
        <div className="fixed inset-0 flex items-center justify-center bg-zinc-600 bg-opacity-80 z-50">
            <div className='mb-24 flex flex-col items-start justify-center bg-gray-900 p-8 rounded-xl drop-shadow-2xl'>
                <div className="flex flex-row w-full justify-end">
                    <button className="text-2xl" onClick={() => {closeModal(false);}}>&times;</button>
                </div>
                <div className="p-4 font-bold">
                    <h1>Are you sure you want to delete this item?</h1>
                </div>
                <div className="p-4">
                    <p>This action will remove this item from the database...</p>
                </div>
                <div className="p-4">
                    <button onClick={() => {closeModal(false);}}  className="pt-2 pb-2 pl-4 pr-4  mr-1 text-gray-900 bg-lime-500 rounded-full w-fit font-bold hover:bg-lime-600">Cancel</button>
                    <button 
                        className="pt-2 pb-2 pl-4 pr-4 mr-1 ml-1 text-white bg-rose-800 rounded-full w-fit font-bold hover:bg-rose-900"
                        onClick={() => {
                            deleteItem()
                        }}
                    >
                        Delete Item
                    </button>
                </div>
            </div>
        </div>
    )
}

export default Modal;
