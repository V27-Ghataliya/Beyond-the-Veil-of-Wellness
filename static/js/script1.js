// =========================================
// Beyond the Veil of Wellness - Custom JavaScript
// =========================================

document.addEventListener('DOMContentLoaded', function() {
    
    // =========================================
    // Navigation Effects
    // =========================================
    
    // Navbar scroll effect
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
    
    // =========================================
    // Form Enhancements
    // =========================================
    
    // Enhanced form validation
    const forms = document.querySelectorAll('.needs-validation');
    
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                
                // Focus on first invalid field
                const firstInvalid = form.querySelector(':invalid');
                if (firstInvalid) {
                    firstInvalid.focus();
                    firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }
            form.classList.add('was-validated');
        });
    });
    
    // Real-time validation feedback
    const formInputs = document.querySelectorAll('.form-control, .form-select');
    
    formInputs.forEach(function(input) {
        input.addEventListener('blur', function() {
            if (this.checkValidity()) {
                this.classList.add('is-valid');
                this.classList.remove('is-invalid');
            } else {
                this.classList.add('is-invalid');
                this.classList.remove('is-valid');
            }
        });
        
        input.addEventListener('input', function() {
            if (this.classList.contains('was-validated')) {
                if (this.checkValidity()) {
                    this.classList.add('is-valid');
                    this.classList.remove('is-invalid');
                } else {
                    this.classList.add('is-invalid');
                    this.classList.remove('is-valid');
                }
            }
        });
    });
    
    // =========================================
    // Interactive Elements
    // =========================================
    
    // Smooth scrolling for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    anchorLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                const offsetTop = targetElement.offsetTop - 80; // Account for fixed navbar
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // =========================================
    // Loading States
    // =========================================
    
    // Button loading state
    const submitButtons = document.querySelectorAll('.submit-btn');
    
    submitButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const form = this.closest('form');
            if (form && form.checkValidity()) {
                this.classList.add('loading');
                
                const spinner = this.querySelector('.spinner-border');
                const text = this.querySelector('.btn-text');
                
                if (spinner) spinner.classList.remove('d-none');
                if (text) text.textContent = 'Processing...';
                
                this.disabled = true;
            }
        });
    });
    
    // =========================================
    // Intersection Observer for Animations
    // =========================================
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                
                // Counter animation for statistics
                if (entry.target.classList.contains('counter')) {
                    animateCounter(entry.target);
                }
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animatedElements = document.querySelectorAll('.feature-card, .counter, .team-card');
    animatedElements.forEach(function(el) {
        observer.observe(el);
    });
    
    // =========================================
    // Counter Animation
    // =========================================
    
    function animateCounter(element) {
        const target = parseInt(element.getAttribute('data-count'));
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;
        
        const timer = setInterval(function() {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            element.textContent = Math.floor(current);
        }, 16);
    }
    
    // =========================================
    // Enhanced Select Dropdowns
    // =========================================
    
    const selectElements = document.querySelectorAll('.form-select');
    
    selectElements.forEach(function(select) {
        // Add custom styling based on selection
        select.addEventListener('change', function() {
            if (this.value) {
                this.classList.add('has-value');
                this.style.background = '#f0fdf4';
            } else {
                this.classList.remove('has-value');
                this.style.background = '#ffffff';
            }
        });
        
        // Custom focus effects
        select.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        
        select.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
        });
    });
    
    // =========================================
    // Tooltip Initialization
    // =========================================
    
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // =========================================
    // Dynamic Background Effects
    // =========================================
    
    // Parallax effect for hero section
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const heroBackground = document.querySelector('.hero-background');
        
        if (heroBackground) {
            const rate = scrolled * -0.5;
            heroBackground.style.transform = `translateY(${rate}px)`;
        }
    });
    
    // =========================================
    // Form Progress Indicator
    // =========================================
    
    function updateFormProgress() {
        const formSelects = document.querySelectorAll('.form-select');
        const totalFields = formSelects.length;
        let filledFields = 0;
        
        formSelects.forEach(function(select) {
            if (select.value) {
                filledFields++;
            }
        });
        
        const progress = (filledFields / totalFields) * 100;
        
        // Update progress bar if exists
        const progressBar = document.querySelector('.form-progress');
        if (progressBar) {
            progressBar.style.width = progress + '%';
        }
        
        // Enable/disable submit button based on completion
        const submitButton = document.querySelector('.submit-btn');
        if (submitButton) {
            if (progress === 100) {
                submitButton.classList.remove('btn-outline-primary');
                submitButton.classList.add('btn-primary');
                submitButton.disabled = false;
            } else {
                submitButton.classList.add('btn-outline-primary');
                submitButton.classList.remove('btn-primary');
            }
        }
    }
    
    // Listen for changes in form fields
    const formFields = document.querySelectorAll('.form-select, .form-control');
    formFields.forEach(function(field) {
        field.addEventListener('change', updateFormProgress);
        field.addEventListener('input', updateFormProgress);
    });
    
    // =========================================
    // Results Page Enhancements
    // =========================================
    
    // Animate confidence meter
    const confidenceMeter = document.querySelector('.progress-bar');
    if (confidenceMeter) {
        setTimeout(function() {
            confidenceMeter.style.transition = 'width 2s ease-in-out';
        }, 500);
    }
    
    // Print functionality
    window.printResults = function() {
        const printContent = document.querySelector('.results-card').innerHTML;
        const printWindow = window.open('', '_blank');
        printWindow.document.write(`
            <html>
                <head>
                    <title>Animal Health Report</title>
                    <style>
                        body { font-family: Arial, sans-serif; margin: 20px; }
                        .text-primary { color: #2563eb !important; }
                        .fw-bold { font-weight: bold; }
                        .mb-3 { margin-bottom: 1rem; }
                        .p-4 { padding: 1.5rem; }
                        .border { border: 1px solid #ccc; }
                        .rounded { border-radius: 8px; }
                    </style>
                </head>
                <body>
                    ${printContent}
                </body>
            </html>
        `);
        printWindow.document.close();
        printWindow.print();
    };
    
    // =========================================
    // Theme Switcher (Optional)
    // =========================================
    
    // Check for saved theme preference or default to light mode
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    
    // Theme toggle functionality
    const themeToggle = document.querySelector('.theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            // Update toggle icon
            const icon = this.querySelector('i');
            if (newTheme === 'dark') {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            } else {
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
            }
        });
    }
    
    // =========================================
    // Performance Optimizations
    // =========================================
    
    // Lazy loading for images
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(function(img) {
        imageObserver.observe(img);
    });
    
    // =========================================
    // Error Handling
    // =========================================
    
    // Global error handler
    window.addEventListener('error', function(e) {
        console.error('Global error:', e.error);
        
        // Show user-friendly error message
        const errorAlert = document.createElement('div');
        errorAlert.className = 'alert alert-danger alert-dismissible fade show position-fixed';
        errorAlert.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
        errorAlert.innerHTML = `
            <i class="fas fa-exclamation-triangle me-2"></i>
            Something went wrong. Please refresh the page or try again.
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(errorAlert);
        
        // Auto-remove after 5 seconds
        setTimeout(function() {
            if (errorAlert.parentNode) {
                errorAlert.remove();
            }
        }, 5000);
    });
    
    // =========================================
    // Accessibility Enhancements
    // =========================================
    
    // Keyboard navigation for custom elements
    const customButtons = document.querySelectorAll('.feature-card, .team-card');
    
    customButtons.forEach(function(element) {
        element.setAttribute('tabindex', '0');
        element.setAttribute('role', 'button');
        
        element.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.click();
            }
        });
    });
    
    // =========================================
    // User Experience Enhancements
    // =========================================
    
    // Auto-save form data (in memory only)
    const formData = {};
    
    formFields.forEach(function(field) {
        // Load saved data
        if (formData[field.name]) {
            field.value = formData[field.name];
        }
        
        // Save data on change
        field.addEventListener('change', function() {
            formData[this.name] = this.value;
        });
    });
    
    // Form reset confirmation
    const resetButtons = document.querySelectorAll('button[type="reset"], .reset-btn');
    
    resetButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to reset the form? All entered data will be lost.')) {
                e.preventDefault();
            } else {
                // Clear saved form data
                Object.keys(formData).forEach(key => delete formData[key]);
            }
        });
    });
    
    // =========================================
    // Analytics and Tracking (Placeholder)
    // =========================================
    
    // Track form interactions
    function trackEvent(action, category, label) {
        // Placeholder for analytics tracking
        console.log(`Event: ${action}, Category: ${category}, Label: ${label}`);
        
        // Example: Google Analytics 4 event tracking
        // gtag('event', action, {
        //     event_category: category,
        //     event_label: label
        // });
    }
    
    // Track form submissions
    forms.forEach(function(form) {
        form.addEventListener('submit', function() {
            trackEvent('form_submit', 'health_check', 'animal_classification');
        });
    });
    
    // Track button clicks
    const trackableButtons = document.querySelectorAll('.btn-primary, .btn-warning');
    trackableButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const buttonText = this.textContent.trim();
            trackEvent('button_click', 'navigation', buttonText);
        });
    });
    
    // =========================================
    // Mobile Optimizations
    // =========================================
    
    // Touch device detection
    function isTouchDevice() {
        return (('ontouchstart' in window) ||
                (navigator.maxTouchPoints > 0) ||
                (navigator.msMaxTouchPoints > 0));
    }
    
    if (isTouchDevice()) {
        document.body.classList.add('touch-device');
        
        // Adjust hover effects for touch devices
        const hoverElements = document.querySelectorAll('.feature-card, .team-card');
        hoverElements.forEach(function(element) {
            element.addEventListener('touchstart', function() {
                this.classList.add('touch-active');
            });
            
            element.addEventListener('touchend', function() {
                setTimeout(() => {
                    this.classList.remove('touch-active');
                }, 150);
            });
        });
    }
    
    // =========================================
    // Performance Monitoring
    // =========================================
    
    // Page load time tracking
    window.addEventListener('load', function() {
        const loadTime = performance.now();
        console.log(`Page loaded in ${Math.round(loadTime)}ms`);
        
        // Track slow loading pages
        if (loadTime > 3000) {
            trackEvent('performance', 'slow_load', `${Math.round(loadTime)}ms`);
        }
    });
    
    // =========================================
    // Utility Functions
    // =========================================
    
    // Debounce function for performance
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func.apply(this, args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
    
    // Throttle function for scroll events
    function throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }
    
    // Copy to clipboard functionality
    window.copyToClipboard = function(text) {
        navigator.clipboard.writeText(text).then(function() {
            showToast('Copied to clipboard!', 'success');
        }).catch(function() {
            showToast('Failed to copy to clipboard', 'error');
        });
    };
    
    // Toast notification system
    window.showToast = function(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
        toast.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
        
        const icon = {
            success: 'fa-check-circle',
            error: 'fa-exclamation-circle',
            warning: 'fa-exclamation-triangle',
            info: 'fa-info-circle'
        }[type] || 'fa-info-circle';
        
        toast.innerHTML = `
            <i class="fas ${icon} me-2"></i>
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(toast);
        
        // Auto-remove after 5 seconds
        setTimeout(function() {
            if (toast.parentNode) {
                toast.remove();
            }
        }, 5000);
    };
    
    // =========================================
    // Initialize Components
    // =========================================
    
    console.log('Beyond the Veil of Wellness - JavaScript initialized successfully');
    
    // Initialize any additional components here
    updateFormProgress();
});

// =========================================
// Service Worker Registration (Optional)
// =========================================

if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/static/js/sw.js')
            .then(function(registration) {
                console.log('SW registered: ', registration);
            })
            .catch(function(registrationError) {
                console.log('SW registration failed: ', registrationError);
            });
    });
}
