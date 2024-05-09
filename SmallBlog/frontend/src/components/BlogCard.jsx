import React from "react";

const BlogCard = ({ id, title, username, content }) => {
  const CONTENT_CHAR_CAP = 250;

  content =
    content.length > CONTENT_CHAR_CAP
      ? content.substring(0, CONTENT_CHAR_CAP) + "..."
      : content;

  return (
    <div className="flex z-[100] flex-col w-full shadow-xl px-5 py-6 rounded-md hover:shadow-2xl hover:-translate-x-3 transition-all duration-500">
      <h2 className="font-bold text-2xl hover:opacity-70 transition-opacity duration-750">
        <a href={`/blogs/${id}`}>{title}</a>
      </h2>
      <div className="mt-1">
        <h3 className="text-sm opacity-60"> {username}</h3>
      </div>
      <div className="mt-2 opacity-90">
        <p> {content} </p>
      </div>
    </div>
  );
};

export default BlogCard;
