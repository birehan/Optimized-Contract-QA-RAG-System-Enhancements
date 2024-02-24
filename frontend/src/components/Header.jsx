const Header = () => {
  return (
    <div>
      <header className="fixed w-full my-7 z-50 md:my-0 md:px-20 md:shadow-3xl md:bg-white md:py-8">
        <div className="mx-4 md:mx-auto max-w-7xl p-4 md:p-0 rounded-full md:rounded-none shadow-3xl bg-white md:shadow-none md:bg-none md">
          <div className="relative z-50 flex justify-between">
            <div className="flex items-center">
              <a aria-label="Home" href="/#">
                <svg
                  width="114"
                  height="40"
                  viewBox="0 0 114 40"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M6.82862 27.4869C3.37929 27.4869 0.583008 24.0207 0.583008 19.7458C0.583008 15.4708 3.37929 12.0046 6.82862 12.0046V27.4869Z"
                    fill="#8A21C4"
                  ></path>
                  <path
                    d="M10.8403 39.2787V0.212769C10.8403 0.212769 24.985 1.05892 29.6049 6.61501C29.6049 16.0281 30.0878 30.7118 10.8403 39.2787Z"
                    fill="#25A7FF"
                  ></path>
                  <path
                    d="M41.8965 27.2106V7.52662H38.1304V30.7623H51.51V27.2106H41.8965Z"
                    fill="#0E1013"
                  ></path>
                  <path
                    d="M54.9836 10.0825H58.7497V6.26526H54.9836V10.0825ZM55.0497 30.7623H58.7167V12.8376H55.0497V30.7623Z"
                    fill="#0E1013"
                  ></path>
                  <path
                    d="M68.0024 27.3765L76.5918 13.4019V12.8376H62.9479V16.2234H70.9426L62.2871 30.2976V30.7623H76.5918V27.3765H68.0024Z"
                    fill="#0E1013"
                  ></path>
                  <path
                    d="M84.4133 27.3765L93.0026 13.4019V12.8376H79.3587V16.2234H87.3535L78.698 30.2976V30.7623H93.0026V27.3765H84.4133Z"
                    fill="#0E1013"
                  ></path>
                  <path
                    d="M109.678 12.8376L104.359 25.3517L98.6768 12.8376H94.7125L102.476 29.4677L102.08 30.3308C100.758 33.1855 100.031 33.8825 97.6857 33.8825H96.133V37.2019H97.95C101.584 37.2019 103.368 35.6086 105.383 31.0942L113.576 12.8376H109.678Z"
                    fill="#0E1013"
                  ></path>
                </svg>
              </a>
              <div className="hidden md:flex items-center justify-between w-full">
                <a
                  className="text-base ml-6 px-3 py-2 hover:text-lizzy-black-65 text-lizzy-black"
                  href="/"
                >
                  Home
                </a>
                <a
                  className="text-base ml-6 px-3 py-2 hover:text-lizzy-black-65 text-lizzy-black"
                  href="/pricing"
                >
                  Pricing
                </a>
                <a
                  className="text-base ml-6 px-3 py-2 hover:text-lizzy-black-65 text-lizzy-black"
                  href="/faq"
                >
                  FAQ
                </a>
              </div>
            </div>
            <div className="hidden md:flex">
              <a
                className="opacity-0 transition-opacity px-5 py-2 mr-4 bg-lizzy-blue text-white hover:text-slate-100 hover:bg-lizzy-blue-65 active:bg-lizzy-blue-65 active:text-blue-100 focus-visible:outline-blue-600 rounded-3xl"
                href="https://login.lizzyai.com/JoinWaitlist"
              >
                Join waitlist
              </a>
              <a
                className="px-5 py-2 text-lizzy-black border-lizzy-black border-solid border rounded-3xl hover:text-lizzy-black-65"
                href="https://login.lizzyai.com/?returnUrl=https://poc.lizzyai.com/"
              >
                Sign in
              </a>
            </div>
            <div className="flex items-center md:hidden">
              <a
                className="group inline-flex items-center justify-center rounded-full py-2 px-4 mr-4 text-sm font-semibold focus:outline-none focus-visible:outline-2 focus-visible:outline-offset-2 bg-lizzy-blue text-white hover:text-slate-100 hover:bg-lizzy-blue-65 active:bg-lizzy-blue-65 active:text-blue-100 focus-visible:outline-blue-600"
                href="https://login.lizzyai.com/JoinWaitlist"
              >
                <span>Join waitlist</span>
              </a>
              <div className="-mr-1 md:hidden">
                <div data-headlessui-state="">
                  <button
                    className="relative z-10 flex h-8 w-8 items-center justify-center [&amp;:not(:focus-visible)]:focus:outline-none"
                    type="button"
                    aria-expanded="false"
                    data-headlessui-state=""
                    id="headlessui-popover-button-:r0:"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      strokeWidth="1.5"
                      stroke="currentColor"
                      aria-hidden="true"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
                      ></path>
                    </svg>
                  </button>
                </div>
                <div className="container"></div>
              </div>
            </div>
          </div>
        </div>
      </header>
    </div>
  );
};

export default Header;
