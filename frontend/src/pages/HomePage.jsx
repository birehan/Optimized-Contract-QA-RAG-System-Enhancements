import { Link } from "react-router-dom";
import Header from "../components/Header";

const HomePage = () => {
  return (
    <div>
      <div>
        <Header />
      </div>

      <section className="relative">
        <div className="relative min-h-screen mx-auto md:mt-0 max-w-7xl px-4 sm:px-6 lg:px-8 pb:12 md:pb-24 pt-36 text-center md:pt-44">
          <h1 className="mx-auto max-w-4xl font-display font-medium tracking-tight text-slate-900 text-5xl md:text-7xl md:max-w-3xl">
            Your AI Contract Assistant
          </h1>
          <p className="w-80 md:w-auto md:max-w-lg mx-auto mt-6 max-w-2xl text-lg tracking-tight text-slate-700">
            The next generation contract AI, right in Microsoft Word. Draft and
            review contracts better and faster!
          </p>

          <div className="relative h-56 mx-auto mt-24 w-[28rem] overflow-hidden " >
  <div className="absolute top-0 left-0">

  <Link
            className="ml-8 relative inline-flex items-center justify-center rounded-full py-4 px-8  text-lg font-semibold focus:outline-none focus-visible:outline-2 focus-visible:outline-offset-2 bg-[#25A7FF] text-white hover:text-slate-100 
            hover:bg-[#25A7FF] active:bg-[#25A7FF] active:text-blue-100 focus-visible:outline-blue-600 md:shadow-2xl 
            md:shadow-[#25A7FF] z-40"
            to="/contract-assistant"
            
          >
            <span>Contract Assistant</span>
          </Link>

  </div>
  <div className="absolute bottom-0 right-0 ">
    
  <Link
            className="mr-8 mb-16 relative inline-flex items-center justify-center rounded-full py-4 px-8  text-lg font-semibold focus:outline-none focus-visible:outline-2 focus-visible:outline-offset-2 
            bg-[#ac62d5] text-white hover:text-slate-100 
            hover:bg-[#ac62d5] active:bg-[#ac62d5] active:text-blue-100 focus-visible:outline-blue-600 md:shadow-2xl 
            md:shadow-[#ac62d5] z-40"
            to="/rag-evaluation"

          >
            <span>Evaluate Assistant</span>
          </Link>
  </div>
</div>
        
          <div className="relative md:hidden flex justify-center z-30 mix-blend-multiply mb-4">
            <div className="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-36 -ml-32 shadow-3xl bg-white rounded-md p-2 text-xs text-lizzy-violet -rotate-12 z-20">
              <span className="absolute top-1 left-1 bg-lizzy-violet w-2 h-2"></span>
              <span className="absolute top-1 -left-2 bg-lizzy-violet w-1 h-1"></span>
              <span className="absolute -top-3 left-2 bg-lizzy-violet w-1 h-1"></span>
              Works on Windows and Mac
            </div>
            <div className="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 ml-40 w-28 shadow-3xl bg-white rounded-md p-2 text-xs text-lizzy-violet rotate-6 z-20">
              <span className="absolute top-1 right-1 bg-lizzy-violet w-2 h-2"></span>
              <span className="absolute top-1 -right-2 bg-lizzy-violet w-1 h-1"></span>
              <span className="absolute -top-3 right-2 bg-lizzy-violet w-1 h-1"></span>
              Free version available
            </div>
            <img
              className="max-w-[262px]"
              src="/assets/artboard-sm-9689d080.png"
            />
          </div>
          <div className="relative hidden md:block">
            <div className="relative">
            
              <video
                loop=""
                controls=""
                poster="/assets/meet-lizzy-poster-56103425.png"
                preload="auto"
                className="relative mx-auto w-full max-w-4xl flex justify-center shadow-3xl rounded-2xl md:mt-32 -mt-24 z-20"
              >
                <source
                  src="/assets/meet-lizzy-a0874e91.mp4"
                  type="video/mp4"
                />
              </video>
              <svg
                width="540"
                height="540"
                viewBox="0 0 540 540"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
                className="absolute z-30 md:w-[250px] md:h-[250px] w-[120px] h-[120px] top-1/2 left-1/2 -translate-y-1/2 -translate-x-1/2 hover:scale-75 transition-transform cursor-pointer"
              >
                <g filter="url(#filter0_d_2337_10349)">
                  <circle cx="270" cy="270" r="145" fill="white"></circle>
                  <path
                    d="M335.048 267.732C336.43 268.929 336.43 271.071 335.048 272.268L244.031 351.091C242.088 352.774 239.067 351.394 239.067 348.823L239.067 191.177C239.067 188.606 242.088 187.226 244.031 188.909L335.048 267.732Z"
                    fill="#25A7FF"
                  ></path>
                </g>
                <defs>
                  <filter
                    id="filter0_d_2337_10349"
                    x="0"
                    y="0"
                    width="540"
                    height="540"
                    filterUnits="userSpaceOnUse"
                    colorInterpolationFilters="sRGB"
                  >
                    <feFlood
                      floodOpacity="0"
                      result="BackgroundImageFix"
                    ></feFlood>

                    <feColorMatrix
                      in="SourceAlpha"
                      type="matrix"
                      values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                      result="hardAlpha"
                    ></feColorMatrix>
                    <feOffset></feOffset>
                    <feGaussianBlur stdDeviation="62.5"></feGaussianBlur>
                    <feColorMatrix
                      type="matrix"
                      values="0 0 0 0 0.717647 0 0 0 0 0.898039 0 0 0 0 1 0 0 0 1 0"
                    ></feColorMatrix>
                    <feBlend
                      mode="normal"
                      in2="BackgroundImageFix"
                      result="effect1_dropShadow_2337_10349"
                    ></feBlend>
                    <feBlend
                      mode="normal"
                      in="SourceGraphic"
                      in2="effect1_dropShadow_2337_10349"
                      result="shape"
                    ></feBlend>
                  </filter>
                </defs>
              </svg>
            </div>
            <img
              src="/assets/artboard-lg-cea88b62.png"
              className="absolute mix-blend-multiply -top-[320px] -left-[85px] w-[511px] z-20"
            />
            <img
              src="/assets/papers-lg-64ab4e3e.png"
              className="absolute z-20 w-[416px] -top-[320px] -right-[62px]"
            />
            <div className="absolute shadow-3xl bg-white rounded-md py-2 px-3 text-base text-lizzy-violet -rotate-12 z-20 -top-[117px] right-[270px]">
              Free forever version available
            </div>
            <div className="absolute shadow-3xl bg-white rounded-md py-2 px-3 text-base text-lizzy-violet rotate-12 z-20 -top-[238px] right-[117px]">
              Works on Windows and Mac
            </div>
          </div>
          <div className="relative md:hidden pb-24">
            <div className="relative">
              <video
                loop=""
                controls=""
                poster="/assets/meet-lizzy-poster-56103425.png"
                preload="auto"
                className="relative mx-auto w-full max-w-4xl flex justify-center shadow-3xl rounded-2xl md:mt-32 -mt-24 z-20"
              >
                <source
                  src="/assets/meet-lizzy-a0874e91.mp4"
                  type="video/mp4"
                />
              </video>
              <svg
                width="540"
                height="540"
                viewBox="0 0 540 540"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
                className="absolute z-30 md:w-[250px] md:h-[250px] w-[120px] h-[120px] top-1/2 left-1/2 -translate-y-1/2 -translate-x-1/2 hover:scale-75 transition-transform cursor-pointer"
              >
                <g filter="url(#filter0_d_2337_10349)">
                  <circle cx="270" cy="270" r="145" fill="white"></circle>

                  <path
                    d="M335.048 267.732C336.43 268.929 336.43 271.071 335.048 272.268L244.031 351.091C242.088 352.774 239.067 351.394 239.067 348.823L239.067 191.177C239.067 188.606 242.088 187.226 244.031 188.909L335.048 267.732Z"
                    fill="#25A7FF"
                  ></path>
                </g>
                <defs>
                  <filter
                    id="filter0_d_2337_10349"
                    x="0"
                    y="0"
                    width="540"
                    height="540"
                    filterUnits="userSpaceOnUse"
                    colorInterpolationFilters="sRGB"
                  >
                    <feFlood
                      floodOpacity="0"
                      result="BackgroundImageFix"
                    ></feFlood>
                    <feColorMatrix
                      in="SourceAlpha"
                      type="matrix"
                      values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                      result="hardAlpha"
                    ></feColorMatrix>
                    <feOffset></feOffset>
                    <feGaussianBlur stdDeviation="62.5"></feGaussianBlur>
                    <feColorMatrix
                      type="matrix"
                      values="0 0 0 0 0.717647 0 0 0 0 0.898039 0 0 0 0 1 0 0 0 1 0"
                    ></feColorMatrix>
                    <feBlend
                      mode="normal"
                      in2="BackgroundImageFix"
                      result="effect1_dropShadow_2337_10349"
                    ></feBlend>
                    <feBlend
                      mode="normal"
                      in="SourceGraphic"
                      in2="effect1_dropShadow_2337_10349"
                      result="shape"
                    ></feBlend>
                  </filter>
                </defs>
              </svg>
            </div>
          </div>
        </div>
        <div className="absolute bottom-0 left-0 w-full md:hidden">
          <div className="w-full h-4 mb-10 mt-10 container-2"></div>
          <div className="w-full h-4 mb-10 mt-10 container-3"></div>
          <div className="w-full h-4 mb-10 mt-10 container-4"></div>
          <div className="w-full h-4 mb-9 mt-10 container-5"></div>
        </div>
        <div className="absolute bottom-0 left-0 w-full hidden md:block">
          <div className="w-full h-4 mb-20 mt-20 container-6 "></div>
          <div className="w-full h-4 mb-20 mt-20 container-7"></div>
          <div className="w-full h-4 mb-20 mt-20 container-8"></div>

          <div className="w-full h-4 mb-11 mt-20 container-9"></div>
        </div>
      </section>
    </div>
  );
};

export default HomePage;
