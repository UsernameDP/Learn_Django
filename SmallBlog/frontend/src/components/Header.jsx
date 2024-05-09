import React, { useEffect, useState } from "react";

const Header = () => {
  const [username, setUsername] = useState(null);

  useEffect(() => {
    fetch("/api/authenticate")
      .then((response) => {
        if (!response.ok) throw new Error("failed to authenticate");

        return response;
      })
      .then((data) => data.json())
      .then((data) => {
        setUsername(data["username"]);
      });
  }, []);

  return (
    <header className="w-full bg-blue-400 shadow-lg">
      <section className="w-full flex py-3">
        <section className="self-center flex-[5] flex">
          <h1 className="mx-auto text-3xl text-white font-bold">
            <a href="/">Small Blog</a>
          </h1>
        </section>
        <section className="self-end px-7 flex justify-center my-auto">
          {username ? (
            <p className="text-white"> {username} </p>
          ) : (
            <a
              href="/api/login"
              className="bg-black rounded-lg px-2 py-1 text-white"
            >
              Log in
            </a>
          )}
        </section>
      </section>
    </header>
  );
};

export default Header;
