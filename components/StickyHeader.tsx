// StickyHeader.tsx
// Section 1: Sticky Header Bar — "Signal Bar" Concept
// Job: Anchor reader, reinforce special window, keep CTA visible
// Asymmetry: Left-heavy text cluster balanced by glowing CTA button right
// Balancing Element: CTA button with champagne glow effect

import { motion } from 'framer-motion';

const StickyHeader = () => {
  return (
    <motion.header
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1] }}
      className="sticky top-0 z-50 w-full"
      style={{
        fontFamily: "'Satoshi Variable', sans-serif",
      }}
    >
      {/* Frosted glass background with warm champagne tint */}
      <div
        className="absolute inset-0 backdrop-blur-md"
        style={{
          background: 'linear-gradient(180deg, rgba(250, 249, 247, 0.95) 0%, rgba(247, 231, 206, 0.08) 100%)',
          borderBottom: '1px solid rgba(27, 77, 74, 0.08)',
        }}
      />

      {/* Content layer */}
      <div className="relative z-10 px-4 py-3 md:px-6 md:py-3">
        <div className="mx-auto flex max-w-6xl flex-col items-center gap-3 md:flex-row md:justify-between md:gap-4">

          {/* Left cluster: Cohort info + scarcity (70% visual weight) */}
          <div className="flex flex-wrap items-center justify-center gap-2 md:justify-start md:gap-3">

            {/* Founding Cohort badge with hand-drawn underline */}
            <div className="relative">
              <span
                className="text-sm font-medium tracking-wide md:text-base"
                style={{
                  color: '#1B4D4A',
                  fontFamily: "'Satoshi Variable', sans-serif",
                  fontWeight: 500,
                }}
              >
                Founding Cohort
              </span>
              {/* Custom SVG: Hand-drawn organic underline */}
              <svg
                className="absolute -bottom-1 left-0 w-full"
                height="4"
                viewBox="0 0 100 4"
                preserveAspectRatio="none"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M0 2.5C15 1 25 3.5 40 2C55 0.5 70 3 85 1.5C92 1 100 2.5 100 2.5"
                  stroke="#C17B7B"
                  strokeWidth="1.5"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  style={{ opacity: 0.7 }}
                />
              </svg>
            </div>

            {/* Custom SVG: Organic hand-drawn divider */}
            <svg
              className="hidden h-4 w-6 md:block"
              viewBox="0 0 24 16"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M4 8C6 6 8 10 12 8C16 6 18 10 20 8"
                stroke="#2D7A75"
                strokeWidth="1.5"
                strokeLinecap="round"
                style={{ opacity: 0.4 }}
              />
            </svg>

            {/* Mobile divider dot */}
            <span
              className="text-sm md:hidden"
              style={{ color: '#8FA5A3' }}
            >
              ·
            </span>

            {/* Spots indicator with pulsing signal dot */}
            <div className="flex items-center gap-1.5">
              {/* Custom SVG: Pulsing seat-cap indicator */}
              <div className="relative flex items-center justify-center">
                <motion.div
                  animate={{
                    scale: [1, 1.4, 1],
                    opacity: [0.6, 0.2, 0.6],
                  }}
                  transition={{
                    duration: 2,
                    repeat: Infinity,
                    ease: 'easeInOut',
                  }}
                  className="absolute h-2.5 w-2.5 rounded-full"
                  style={{ backgroundColor: '#C17B7B' }}
                />
                <div
                  className="relative h-1.5 w-1.5 rounded-full"
                  style={{ backgroundColor: '#C17B7B' }}
                />
              </div>
              <span
                className="text-sm font-medium md:text-base"
                style={{
                  color: '#1B4D4A',
                  fontWeight: 500,
                }}
              >
                ~10 Spots
              </span>
            </div>

            {/* Divider */}
            <span
              className="text-sm"
              style={{ color: '#8FA5A3' }}
            >
              ·
            </span>

            {/* Deadline */}
            <span
              className="text-sm md:text-base"
              style={{
                color: '#5A7A78',
                fontWeight: 400,
              }}
            >
              Black Friday Pricing Ends Dec 14
            </span>
          </div>

          {/* Right: CTA Button with champagne glow (balancing element) */}
          <motion.a
            href="#join"
            whileHover={{
              scale: 1.02,
              boxShadow: '0 4px 20px rgba(212, 175, 55, 0.25), 0 0 0 1px rgba(212, 175, 55, 0.15)',
            }}
            whileTap={{ scale: 0.98 }}
            transition={{ type: 'spring', stiffness: 400, damping: 20 }}
            className="relative flex items-center gap-2 rounded-full px-5 py-2 text-sm font-medium transition-colors md:px-6 md:py-2.5 md:text-base"
            style={{
              backgroundColor: '#1B4D4A',
              color: '#FAF9F7',
              fontWeight: 500,
              boxShadow: '0 2px 12px rgba(27, 77, 74, 0.15), 0 0 0 1px rgba(247, 231, 206, 0.2)',
            }}
          >
            See If It's a Fit
            {/* Subtle arrow hint */}
            <svg
              className="h-3.5 w-3.5 transition-transform group-hover:translate-x-0.5"
              viewBox="0 0 14 14"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M2 7H12M12 7L8 3M12 7L8 11"
                stroke="currentColor"
                strokeWidth="1.5"
                strokeLinecap="round"
                strokeLinejoin="round"
                style={{ opacity: 0.8 }}
              />
            </svg>
          </motion.a>
        </div>
      </div>
    </motion.header>
  );
};

export default StickyHeader;
