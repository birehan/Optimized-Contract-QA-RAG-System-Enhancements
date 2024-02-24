const CreateChatForm = () => {
  return (
    <form
      className="bg-white flex items-center justify-center"
      id="wishlist-form"
    >
      <div className="bg-white border border-gray-200 rounded-lg p-8 join-waitlist-box box-border shadow-welcome">
        <a href="#" className="flex">
          <span>
            <img
              src="/images/back-icon.svg"
              className="join-waitlist-back-icon"
              alt=""
            />
          </span>
          <span className="text-primary hover:text-hover font-sans"> Back</span>
        </a>
        <div className="flex font-sans justify-center font-semibold text-2xl pt-2 bg-white">
          <h1>Join Waitlist</h1>
        </div>
        <div className="flex justify-center">
          <p className="justify-center text-center font-normal text-secondary w-full text-sm font-sans pt-2 px-8">
            Lizzy is in closed beta. If you wish to join the Beta Waitlist,
            please fill this form. We’ll reach out as soon as you are selected
          </p>
        </div>

        <div className="">
          <div className="flex justify-end items-center relative pt-2 px-6">
            <input
              placeholder="Full Name"
              id="fullName"
              required=""
              className="text-black placeholder-gray-400 font-sans font-normal w-full px-4 py-2.5 mt-2 text-base transition duration-500 ease-in-out transform border-transparent rounded-lg bg-input focus:border-blue-500 focus:bg-white focus:outline-none focus:shadow-outline focus:ring-2 ring-offset-current ring-offset-2"
            />
            <img
              src="/images/Union.svg"
              id="clearIcon1"
              className="absolute cursor-pointer union-margin w-3 pt-2"
              alt="Clear Icon"
            />
          </div>

          <div className="flex justify-end items-center relative px-6">
            <input
              placeholder="Email"
              id="email"
              type="email"
              required=""
              className="text-black placeholder-gray-400 font-sans font-normal w-full px-4 py-2.5 mt-2 text-base transition duration-500 ease-in-out transform rounded-lg bg-input border focus:bg-white focus:outline-none focus:shadow-outline focus:ring-2 ring-offset-current ring-offset-2"
            />
            <img
              src="/images/Union.svg"
              id="clearIcon"
              className="absolute cursor-pointer union-margin w-3 pt-2"
              alt="Clear Icon"
            />
          </div>
          <div className="flex justify-end items-center relative px-6">
            <input
              placeholder="Your website"
              id="website"
              required=""
              className="text-black placeholder-gray-400 font-sans font-normal w-full px-4 py-2.5 mt-2 text-base transition duration-500 ease-in-out transform border-transparent rounded-lg bg-input focus:border-blue-500 focus:bg-white focus:outline-none focus:shadow-outline focus:ring-2 ring-offset-current ring-offset-2"
            />
            <img
              src="/images/Union.svg"
              id="clearIcon2"
              className="absolute cursor-pointer union-margin w-3 pt-2"
              alt="Clear Icon"
            />
          </div>

          <div className="flex justify-end items-start relative px-6">
            <div className="grow-wrap w-full ">
              <textarea
                placeholder="Shortly describe your interest"
                id="description"
                required=""
                className="px-4 grow-wrap text-black w-full placeholder-gray-400 font-sans font-normal  py-2.5 mt-2 text-base transition duration-500 ease-in-out transform border-transparent rounded-lg bg-input focus:border-blue-500 focus:bg-white focus:outline-none focus:shadow-outline focus:ring-2 ring-offset-current ring-offset-2"
                name="text"
              ></textarea>
            </div>
            <img
              src="/images/Union.svg"
              id="clearIcon3"
              className="absolute cursor-pointer union-margin w-3 pt-5"
              alt="Clear Icon"
            />
         
          </div>
        </div>
        <div className="flex justify-end submit-center relative mt-5 px-6">
          <button
            id="signInButton"
            type="submit"
            className="flex justify-center text-cneter text-white w-full hover:bg-blue-300 focus:ring-4  rounded-lg px-3 py-2 text-center items-center bg-primary font-sans font-semibold text-base h-11"
          >
            Submit Form
          </button>
        </div>
        <div className="flex justify-end items-center relative font-sans text-xs mt-3 px-6">
          <p className="text-center font-normal text-gray-700 w-full">
            By using Lizzy I agree to its
            <span>
              <a href="https://lizzyai.com/terms" className="text-primary">
                {" "}
                Terms{" "}
              </a>
            </span>
            and
            <span>
              <a href="https://lizzyai.com/policy" className="text-primary">
                Privacy Policy{" "}
              </a>
            </span>
          </p>
        </div>
      </div>
    </form>
  );
};

export default CreateChatForm;
