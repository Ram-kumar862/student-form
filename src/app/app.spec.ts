import { TestBed } from '@angular/core/testing';
import { App } from './app';

describe('App', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [App],
    })
      .compileComponents();
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(App);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it('should render the registration form and its required fields', async () => {
    const fixture = TestBed.createComponent(App);
    await fixture.whenStable();
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('h1')?.textContent).toContain('Student Registration Form');
    expect(compiled.querySelector('select[name="course"]')).toBeTruthy();
    expect(compiled.querySelector('input[type="date"][name="dob"]')).toBeTruthy();
    expect(compiled.querySelector('input[name="email"]')?.getAttribute('pattern')).toContain(
      '@gmail',
    );
    expect(compiled.querySelector('.country-code')?.textContent).toContain('+91');
  });

  it('should show an alert when email and phone are missing', async () => {
    const fixture = TestBed.createComponent(App);
    await fixture.whenStable();
    const compiled = fixture.nativeElement as HTMLElement;
    const form = compiled.querySelector('form');

    form?.dispatchEvent(new Event('submit', { bubbles: true, cancelable: true }));
    fixture.detectChanges();

    expect(compiled.querySelector('[role="alert"]')?.textContent).toContain('Email is required.');
    expect(compiled.querySelector('[role="alert"]')?.textContent).toContain(
      'Phone number is required.',
    );
  });
});
