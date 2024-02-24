import React, { Fragment } from "react";
import { Controller, useFormContext } from "react-hook-form";
import { Menu, Transition } from "@headlessui/react";
import { ChevronDownIcon } from "@heroicons/react/20/solid";

interface Option {
  key: string;
  value: string;
}

interface Props {
  label: string;
  items: Option[];
  name: string;
}

function classNames(...classes: string[]) {
  return classes.filter(Boolean).join(" ");
}

const DropDownInput: React.FC<Props> = ({ label, items, name }) => {
  const { control } = useFormContext();

  return (
    <div className="w-full">
      <label className="block text-sm font-medium leading-6 text-gray-600">
        {label}
      </label>

      <Controller
        name={name}
        control={control}
        rules={{ required: true }} // Add validation rules here
        render={({ field, fieldState: { invalid } }) => (
          <Menu
            as="div"
            className="relative inline-block text-left mt-2 w-full"
          >
            <div>
              <Menu.Button
                className={classNames(
                  "inline-flex w-full justify-between gap-x-1.5 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50",
                  invalid ? "ring-red-500" : "" // Apply red border on validation error
                )}
              >
                {field.value
                  ? items.find((item) => item.key === field.value)?.value ||
                    "Options"
                  : "Options"}
                <ChevronDownIcon
                  className="-mr-1 h-5 w-5 text-gray-400"
                  aria-hidden="true"
                />
              </Menu.Button>
            </div>

            <Transition
              as={Fragment}
              //   show={formState.menuOpen} // Use a state variable to control menu visibility
              enter="transition ease-out duration-100"
              enterFrom="transform opacity-0 scale-95"
              enterTo="transform opacity-100 scale-100"
              leave="transition ease-in duration-75"
              leaveFrom="transform opacity-100 scale-100"
              leaveTo="transform opacity-0 scale-95"
            >
              <Menu.Items className="absolute right-0 z-10 mt-2 w-full origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                <div className="py-1">
                  {items.map((item) => (
                    <Menu.Item key={item.key}>
                      {({ active }) => (
                        <button
                          type="button"
                          onClick={() => {
                            field.onChange(item.key); // Set the selected value in React Hook Form
                          }}
                          className={classNames(
                            active
                              ? "bg-gray-100 text-gray-900"
                              : "text-gray-700",
                            "block w-full px-4 py-2 text-left text-sm"
                          )}
                        >
                          {item.value}
                        </button>
                      )}
                    </Menu.Item>
                  ))}
                </div>
              </Menu.Items>
            </Transition>

            {invalid ? (
              <p className="mt-2 text-sm text-red-500" role="alert">
                {label} is required.
              </p>
            ) : (
              ""
            )}
          </Menu>
        )}
      />
    </div>
  );
};

export default DropDownInput;
