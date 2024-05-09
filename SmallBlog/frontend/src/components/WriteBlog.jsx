import React, { useState } from "react";

const WriteBlog = () => {
  const [title, setTitle] = useState(""); // State for the title
  const [content, setContent] = useState(""); // State for the content

  // Handler for changes to the title input
  const handleTitleChange = (event) => {
    setTitle(event.target.value);
  };

  // Handler for changes to the content input
  const handleContentChange = (event) => {
    setContent(event.target.value);
  };

  const handleSubmit = (event) => {
    fetch("/api/addPost", {
      method: "POST",
      body: JSON.stringify({ title: title, content: content })
    })
      .catch((err) => {
        throw err;
      })
      .then((data) => {
        return data.json();
      })
      .then((data) => console.log(data));
  };

  return (
    <div className="prose mx-auto flex flex-col gap-5">
      <input
        type="text"
        value={title}
        onChange={handleTitleChange}
        className="  border-2"
        placeholder="Enter title here"
      />

      <textarea
        className="border-2"
        placeholder="Enter content here"
        rows={25}
        value={content}
        onChange={handleContentChange}
      ></textarea>

      <button
        className="w-full bg-blue-500 text-white rounded-sm"
        onClick={handleSubmit}
      >
        Submit
      </button>
    </div>
  );
};

export default WriteBlog;
