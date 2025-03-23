import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import { Input } from "@/components/ui/input";
import { Eye, EyeOff } from "lucide-react";
import React from "react";

export default function Cinematch(): JSX.Element {
  // State for password visibility toggle
  const [showPassword, setShowPassword] = React.useState(false);

  return (
    <main className="flex justify-center items-center min-h-screen bg-transparent">
      <div className="w-full max-w-[1366px] h-[854px] flex">
        {/* Left side with illustrations */}
        <section className="relative w-[753px] h-full bg-[url(/clip-path-group-6.png)] bg-cover bg-center">
          <div className="absolute w-[719px] h-[601px] top-[126px] left-[11px] bg-[url(/mask-group.png)] bg-cover bg-center">
            {/* Movie-related illustrations */}
            <img
              className="absolute w-[172px] h-[63px] top-[510px] left-[455px]"
              alt="Cinematch logo"
              src=""
            />
          </div>
          <img
            className="absolute w-[116px] h-[68px] top-6 left-[27px]"
            alt="Brand logo"
            src=""
          />
        </section>

        {/* Right side with login form */}
        <section className="relative w-[548px] h-full flex flex-col justify-center items-center p-8">
          <div className="w-full max-w-md">
            {/* Login header */}
            <div className="mb-6 text-center">
              <h1 className="text-4xl font-bold mb-4">Login</h1>
              <p className="text-muted-foreground">
                Don't have an account yet?{" "}
                <a
                  href="#"
                  className="text-primary font-semibold hover:underline"
                >
                  Sign Up
                </a>
              </p>
            </div>

            {/* Login form */}
            <form className="space-y-4">
              {/* Username/Email field */}
              <div className="relative">
                <Input
                  type="text"
                  placeholder="Username or Email"
                  className="pl-10 py-6 rounded-md"
                />
                <div className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground">
                  <svg
                    width="16"
                    height="16"
                    viewBox="0 0 24 24"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M12 11C14.2091 11 16 9.20914 16 7C16 4.79086 14.2091 3 12 3C9.79086 3 8 4.79086 8 7C8 9.20914 9.79086 11 12 11Z"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    />
                    <path
                      d="M20 21C20 16.5817 16.4183 13 12 13C7.58172 13 4 16.5817 4 21"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    />
                  </svg>
                </div>
              </div>

              {/* Password field */}
              <div className="relative">
                <Input
                  type={showPassword ? "text" : "password"}
                  placeholder="Password"
                  className="pl-10 py-6 rounded-md"
                />
                <div className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground">
                  <svg
                    width="16"
                    height="16"
                    viewBox="0 0 24 24"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <rect
                      x="3"
                      y="11"
                      width="18"
                      height="11"
                      rx="2"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    />
                    <path
                      d="M7 11V7C7 4.23858 9.23858 2 12 2C14.7614 2 17 4.23858 17 7V11"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    />
                  </svg>
                </div>
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-muted-foreground"
                >
                  {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                </button>
              </div>

              {/* Remember me and forgot password */}
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-2">
                  <Checkbox id="remember" />
                  <label
                    htmlFor="remember"
                    className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                  >
                    Keep me logged in
                  </label>
                </div>
                <a href="#" className="text-sm text-primary hover:underline">
                  Forgot Password
                </a>
              </div>

              {/* Login buttons */}
              <Button
                type="submit"
                className="w-full py-6 bg-[#B02E5F] hover:bg-[#9a2652] text-white"
              >
                LOGIN
              </Button>
              <Button
                type="button"
                variant="outline"
                className="w-full py-6 bg-[#0A4B6C] hover:bg-[#083a54] text-white border-none"
              >
                LOGIN AS A GUEST
              </Button>
            </form>
          </div>
        </section>
      </div>
    </main>
  );
}