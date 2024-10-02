"use client";
import { useState } from "react";

export default function Home() {
	const [videoUrl, setVideoUrl] = useState("");
	const [response, setResponse] = useState<string | null>(null);

	const handleSubmit = async (e: React.FormEvent) => {
		e.preventDefault();

		// Call your API here
		await fetch("/api/demo", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ videoUrl }),
		});

		// Display a message that the video has been sent for processing
		setResponse("Video Sent For Processing");

		// Clear the input field
		setVideoUrl("");

		// Clear the message after 500ms
		setTimeout(() => {
			setResponse(null);
		}, 1000);
	};

	return (
		<div className="flex flex-col min-h-screen bg-black text-white">
			{/* Header */}
			<header className="w-full py-6 bg-gray-900 text-center border-b border-green-500 shadow-lg">
				<h1 className="text-4xl font-extrabold tracking-wide uppercase">
					The Eagle Eye
				</h1>
				<p className="text-md font-light mt-2 text-gray-300">
					Eyes on Every Corner, Safety in Every Moment
				</p>
			</header>

			{/* Main Content */}
			<main className="flex-grow flex flex-col items-center justify-center p-4">
				{/* Features */}
				<section className="mt-10 w-full max-w-4xl">
					<h2 className="text-3xl font-semibold text-center text-green-500 tracking-widest mb-6">
						Features
					</h2>
					<div className="mt-4 grid grid-cols-1 md:grid-cols-2 gap-8">
						<div className="bg-gray-800 p-6 rounded-lg shadow-md transform transition-transform duration-300 hover:scale-105 border border-gray-700">
							<h3 className="text-xl font-bold text-white mb-4">
								Current Features
							</h3>
							<ul className="text-gray-300 list-disc list-inside">
								<li>
									Real-time crime detection through
									surveillance cameras
								</li>
								<li>Immediate alerts to local authorities</li>
							</ul>
						</div>

						<div className="bg-gray-800 p-6 rounded-lg shadow-md transform transition-transform duration-300 hover:scale-105 border border-gray-700">
							<h3 className="text-xl font-bold text-white mb-4">
								Future Features
							</h3>
							<ul className="text-gray-300 list-disc list-inside">
								<li>
									Tracking of fleeing suspects through camera
									networks
								</li>
								<li>Predictive analysis to prevent crimes</li>
							</ul>
						</div>
					</div>
				</section>

				{/* Demo Section */}
				<section className="mt-16 w-full max-w-lg">
					<h2 className="text-3xl font-semibold text-center text-green-500 tracking-widest mb-6">
						See a Demo
					</h2>
					<form
						onSubmit={handleSubmit}
						className="mt-4 flex flex-col space-y-4"
					>
						<input
							type="url"
							className="p-4 bg-gray-800 border border-green-500 text-white placeholder-gray-500 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
							placeholder="Enter video URL"
							value={videoUrl}
							onChange={(e) => setVideoUrl(e.target.value)}
							required
						/>
						<button
							type="submit"
							className="bg-green-500 text-white py-3 rounded-lg shadow-md hover:bg-green-600 transition-all duration-300"
						>
							Submit
						</button>
					</form>

					{/* Response Display */}
					{response && (
						<div className="mt-6 p-4 bg-green-800 bg-opacity-30 text-white rounded-lg border border-green-500 shadow-lg text-center text-lg font-semibold">
							{response}
						</div>
					)}
				</section>
			</main>

			{/* Footer */}
			<footer className="w-full py-6 text-center bg-gray-900 text-gray-500 mt-10 border-t border-green-500">
				<p>© 2024 The Eagle Eye. All rights reserved.</p>
			</footer>
		</div>
	);
}
