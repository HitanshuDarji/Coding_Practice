import Link from "next/link";

export default function Navigation() {
    return (
        <div>
            <div>
                <button className="bg-red-600 p-4 rounded-md">
                    <Link href="/table-view">View Table</Link>
                </button>
            </div>
        </div>
    );
}