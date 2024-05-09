import React, { useEffect, useState } from "react";

const createNavigation = (name, path) => {
  return { name: name, path: path };
};

const SidePopup = () => {
  const [open, setOpen] = useState(false);
  const [navigations, setNavigations] = useState([
    createNavigation("Home", "/")
  ]);

  useEffect(() => {
    fetch("/api/authenticate")
      .catch((err) => {
        throw err;
      })
      .then((data) => data.json())
      .then((data) => {
        setNavigations([
          createNavigation("Home", "/"),
          createNavigation("Write", "/write")
        ]);
      });
  }, []);

  const onClick = () => {
    setOpen((open) => !open);
  };

  return (
    <div className="absolute right-0 h-full flex z-[500]">
      <section className="my-auto flex">
        <div className="flex bg-blue-500 flex-row">
          <div className="bg-blue-500 rounded-tl-lg rounded-bl-lg text-white text-4xl text-center flex border-r-white border-r-2">
            <button
              onClick={onClick}
              className=""
            >
              {"<"}
            </button>
          </div>
          <div
            className={`flex-col text-white justify-between items-center gap-2 py-16 px-5 z-[100] ${
              open ? "flex" : "hidden"
            }`}
          >
            {navigations.map((navigation, index) => {
              return (
                <a
                  href={navigation.path}
                  key={index}
                >
                  {navigation.name}
                </a>
              );
            })}
          </div>
        </div>
      </section>
    </div>
  );
};

export default SidePopup;
